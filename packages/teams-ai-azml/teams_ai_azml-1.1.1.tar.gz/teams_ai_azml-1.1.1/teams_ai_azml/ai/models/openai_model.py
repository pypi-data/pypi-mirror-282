"""
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""

from __future__ import annotations

import json
import os
import ssl
import urllib.request
from dataclasses import dataclass
from logging import Logger
from typing import List, Optional, Union

import openai
from botbuilder.core import TurnContext
from openai.types import chat

from ...state import MemoryBase
from ..prompts.message import Message
from ..prompts.prompt_functions import PromptFunctions
from ..prompts.prompt_template import PromptTemplate
from ..tokenizers import Tokenizer
from .prompt_completion_model import PromptCompletionModel
from .prompt_response import PromptResponse


@dataclass
class OpenAIModelOptions:
    """
    Options for configuring an `OpenAIModel` to call an OpenAI hosted model.
    """

    api_key: str
    "API key to use when calling the OpenAI API."

    default_model: str
    "Default model to use for completions."

    endpoint: Optional[str] = None
    "Optional. Endpoint to use when calling the OpenAI API."

    organization: Optional[str] = None
    "Optional. Organization to use when calling the OpenAI API."

    logger: Optional[Logger] = None
    "Optional. When set the model will log requests"


@dataclass
class AzureOpenAIModelOptions:
    """
    Options for configuring an `OpenAIModel` to call an Azure OpenAI hosted model.
    """

    api_key: str
    "API key to use when making requests to Azure OpenAI."

    default_model: str
    "Default name of the Azure OpenAI deployment (model) to use."

    endpoint: str
    "Deployment endpoint to use."

    api_version: str = "2023-05-15"
    "Optional. Version of the API being called. Defaults to `2023-05-15`."

    organization: Optional[str] = None
    "Optional. Organization to use when calling the OpenAI API."

    logger: Optional[Logger] = None
    "Optional. When set the model will log requests"


class OpenAIModel(PromptCompletionModel):
    """
    A `PromptCompletionModel` for calling OpenAI and Azure OpenAI hosted models.
    """

    _options: Union[OpenAIModelOptions, AzureOpenAIModelOptions]
    _client: openai.AsyncOpenAI

    @property
    def options(self) -> Union[OpenAIModelOptions, AzureOpenAIModelOptions]:
        return self._options

    def __init__(self, options: Union[OpenAIModelOptions, AzureOpenAIModelOptions]) -> None:
        """
        Creates a new `OpenAIModel` instance.

        Args:
            options (OpenAIModelOptions | AzureOpenAIModelOptions): model options.
        """

        self._options = options
        if isinstance(options, OpenAIModelOptions):
            self._client = openai.AsyncOpenAI(
                api_key=options.api_key,
                base_url=options.endpoint,
                organization=options.organization,
                default_headers={"User-Agent": self.user_agent},
            )
        elif isinstance(options, AzureOpenAIModelOptions):
            self._client = openai.AsyncAzureOpenAI(
                api_key=options.api_key,
                api_version=options.api_version,
                azure_endpoint=options.endpoint,
                azure_deployment=options.default_model,
                organization=options.organization,
                default_headers={"User-Agent": self.user_agent},
            )

    async def complete_prompt(
        self,
        context: TurnContext,
        memory: MemoryBase,
        functions: PromptFunctions,
        tokenizer: Tokenizer,
        template: PromptTemplate,
    ) -> PromptResponse[str]:
        max_tokens = template.config.completion.max_input_tokens
        model = (
            template.config.completion.model
            if template.config.completion.model is not None
            else self._options.default_model
        )
        res = await template.prompt.render_as_messages(
            context=context,
            memory=memory,
            functions=functions,
            tokenizer=tokenizer,
            max_tokens=max_tokens,
        )

        if res.too_long:
            return PromptResponse[str](
                status="too_long",
                error=f"""
                the generated chat completion prompt had a length of {res.length} tokens 
                which exceeded the max_input_tokens of {max_tokens}
                """,
            )

        if self._options.logger is not None:
            self._options.logger.debug(f"PROMPT:\n{res.output}")

        messages: List[chat.ChatCompletionMessageParam] = []

        for msg in res.output:
            param: Union[
                chat.ChatCompletionUserMessageParam,
                chat.ChatCompletionAssistantMessageParam,
                chat.ChatCompletionSystemMessageParam,
            ] = chat.ChatCompletionUserMessageParam(
                role="user",
                content=msg.content if msg.content is not None else "",
            )

            if msg.name:
                param["name"] = msg.name

            if msg.role == "assistant":
                param = chat.ChatCompletionAssistantMessageParam(
                    role="assistant",
                    content=msg.content if msg.content is not None else "",
                )

                if msg.name:
                    param["name"] = msg.name
            elif msg.role == "system":
                param = chat.ChatCompletionSystemMessageParam(
                    role="system",
                    content=msg.content if msg.content is not None else "",
                )

                if msg.name:
                    param["name"] = msg.name

            messages.append(param)

        try:
            if self._options.endpoint is not None and self._options.api_key is not None:

                def allow_self_signed_https(allowed):
                    # bypass the server certificate verification on client side
                    if (
                        allowed
                        and not os.environ.get("PYTHONHTTPSVERIFY", "")
                        and getattr(ssl, "_create_unverified_context", None)
                    ):
                        ssl._create_default_https_context = ssl._create_unverified_context

                allow_self_signed_https(
                    True
                )  # this line is needed if you use self-signed certificate in your scoring service.

                # Request data goes here
                # The example below assumes JSON formatting which may be updated
                # depending on the format your endpoint expects.
                # More information can be found here:
                # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script

                chat_history = []
                if "chat_history" in memory["conversation"].keys():
                    for i,k in zip(memory.conversation["chat_history"][0::2], memory.conversation["chat_history"][1::2]):
                        dict_={"inputs":None, "outputs": None}
                        user_role=i.role
                        user_content=i.content
                        assistant_role=k.role
                        assistant_content=k.content
                        if "user" == user_role:
                            dict_["inputs"] = {"question": user_content}
                        if "assistant" == assistant_role:
                            dict_["outputs"] = {"answer": assistant_content}
                        chat_history.append(dict_)
                data = {"chat_history": chat_history, "question": msg.content}

                body = str.encode(json.dumps(data))

                scoring_uri = self._options.endpoint
                api_key = self._options.api_key

                if not api_key:
                    raise Exception("A key should be provided to invoke the endpoint")
                # The azureml-model-deployment header will force the request to go to
                # a specific deployment.
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": ("Bearer " + api_key),
                    "azureml-model-deployment": model,
                }

                req = urllib.request.Request(scoring_uri, body, headers)

                try:
                    response = urllib.request.urlopen(req)

                    result = response.read()
                except urllib.error.HTTPError as error:
                    self._options.logger.error(
                        "The request failed with status code: %s", str(error.code)
                    )
                    self._options.logger.error(
                        "The request failed with status code: %s", str(error.info())
                    )
                    self._options.logger.error(
                        "The request failed with status code: %s",
                        str(error.read().decode("utf8", "ignore")),
                    )

                input: Optional[Message] = None
                res_output = json.loads(result.decode("utf-8"))["answer"]
                return PromptResponse[str](
                    input=input, message=Message(role="assistant", content=res_output)
                )
            else:
                completion = await self._client.chat.completions.create(
                    messages=messages,
                    model=model,
                    presence_penalty=template.config.completion.presence_penalty,
                    frequency_penalty=template.config.completion.frequency_penalty,
                    top_p=template.config.completion.top_p,
                    temperature=template.config.completion.temperature,
                    max_tokens=max_tokens,
                )

                if self._options.logger is not None:
                    self._options.logger.debug("COMPLETION:\n%s", completion.model_dump_json())

                input: Optional[Message] = None
                output_length = len(res.output)

                if output_length > 0 and res.output[output_length - 1].role == "user":
                    input = res.output[output_length - 1]

                return PromptResponse[str](
                    input=input,
                    message=Message(
                        role=completion.choices[0].message.role,
                        content=completion.choices[0].message.content,
                    ),
                )
        except openai.APIError as err:
            if self._options.logger is not None:
                self._options.logger.error("ERROR:\n%s", json.dumps(err.body))
            return PromptResponse[str](
                status="error",
                error=f"""
                The chat completion API returned an error 
                status of {err.code}: {err.message}
                """,
            )
