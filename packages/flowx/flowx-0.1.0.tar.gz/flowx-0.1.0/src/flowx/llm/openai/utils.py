from typing import Iterator, Tuple, List, Dict, Any, Type, get_args

from openai import Stream
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionSystemMessageParam, \
    ChatCompletionUserMessageParam, ChatCompletionAssistantMessageParam, ChatCompletionToolMessageParam, \
    ChatCompletionMessageToolCallParam
from openai.types.chat.chat_completion_chunk import Choice as ChoiceChunk, ChatCompletionChunk
from openai.types.chat.chat_completion import Choice, ChatCompletion
from pydantic import BaseModel

from flowx.llm.llm import ChatResult, TokenUsage, ToolChoice, ToolChoiceLiteral
from flowx.messages.chat_message import ChatMessage, Role, ToolCall, ChatMessageChunk, ToolCallChunk
from flowx.tool import Tool


def to_openai_message(message: ChatMessage) -> ChatCompletionMessageParam:
    if message.role == Role.SYSTEM:
        return ChatCompletionSystemMessageParam(role="system", content=message.content or "")
    if message.role == Role.USER:
        return ChatCompletionUserMessageParam(role="user", content=message.content or "")
    if message.role == Role.ASSISTANT:
        msg = ChatCompletionAssistantMessageParam(role="assistant", content=message.content)
        tool_calls: List[ChatCompletionMessageToolCallParam] = []
        for tool_call in message.tool_calls or []:
            tool_calls.append(tool_call.model_dump())  # type: ignore[arg-type]
        if tool_calls:
            msg["tool_calls"] = tool_calls
        return msg
    if message.role == Role.TOOL:
        assert message.tool_call_id
        return ChatCompletionToolMessageParam(role="tool",
                                              content=message.content or "",
                                              tool_call_id=message.tool_call_id)
    raise ValueError(f"message: {message}")


def message_from_openai_choice(choice: Choice) -> ChatMessage:
    message = ChatMessage(role=Role.from_name(choice.message.role),
                          content=choice.message.content,
                          finish_reason=choice.finish_reason)
    tool_calls = list(map(lambda tool_call: ToolCall(**tool_call.model_dump()), choice.message.tool_calls or []))
    if tool_calls:
        message.tool_calls = tool_calls
    return message


def message_chunk_from_openai_choice(choice_chunk: ChoiceChunk) -> ChatMessageChunk:
    role = Role.from_name(choice_chunk.delta.role) if choice_chunk.delta.role else None
    message_chunk = ChatMessageChunk(role=role,
                                     content=choice_chunk.delta.content,
                                     finish_reason=choice_chunk.finish_reason)
    tool_calls = list(map(lambda tool_call: ToolCallChunk(**tool_call.model_dump()),
                          choice_chunk.delta.tool_calls or []))
    if tool_calls:
        message_chunk.tool_calls = tool_calls
    return message_chunk


def chat_result_from_openai(chat_completion: ChatCompletion | Stream[ChatCompletionChunk]) -> ChatResult:
    result = ChatResult()

    if isinstance(chat_completion, ChatCompletion):
        for choice in chat_completion.choices:
            result.messages.append(message_from_openai_choice(choice))
            if chat_completion.usage:
                result.usage = TokenUsage(**chat_completion.usage.model_dump())
    else:
        def to_message_stream() -> Iterator[Tuple[ChatMessageChunk, TokenUsage | None]]:
            for completion_chunk in chat_completion:
                usage = TokenUsage(**completion_chunk.usage.model_dump()) if completion_chunk.usage else None
                if completion_chunk.choices:
                    chunk = message_chunk_from_openai_choice(completion_chunk.choices[0])
                else:
                    chunk = ChatMessageChunk()
                yield chunk, usage

        result.message_stream = to_message_stream()
    return result


def get_tool_by_pydantic(pydantic_class: Type[BaseModel]) -> Dict[str, Any]:
    schema = pydantic_class.model_json_schema()
    function = {
        "name": schema.pop("title"),
        "description": schema.pop("description"),
        "parameters": schema
    }
    return {"type": "function", "function": function}


def get_tool_choice_by_pydantic(pydantic_class: Type[BaseModel]) -> str | dict:
    return {"type": "function", "function": {"name": pydantic_class.schema()["title"]}}


def tool_to_openai(tool: Tool) -> Dict[str, Any]:
    return get_tool_by_pydantic(tool.args_schema)


def tools_to_openai(tools: List[Tool]) -> List[Dict[str, Any]]:
    return list(map(tool_to_openai, tools))


def tool_choice_to_openai(tool_choice: ToolChoice, tools: List[Tool] | None = None):
    tool_choice = "required" if tool_choice == "any" else tool_choice
    if tool_choice in get_args(ToolChoiceLiteral):
        return tool_choice

    for tool in tools or []:
        if tool.name == tool_choice:
            return get_tool_choice_by_pydantic(tool.args_schema)

    tool_names = list(map(lambda tool_: tool_.name, tools or []))
    raise ValueError(f"""Error tool choice: "{tool_choice}" not in tools: {tool_names}""")
