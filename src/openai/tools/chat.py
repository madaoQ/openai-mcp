# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Chat completion tools for OpenAI."""

from __future__ import annotations

from typing import Any

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from openai.guards import (
    validate_max_tokens,
    validate_message_content,
    validate_model,
    validate_temperature,
)
from openai.request import request
from openai.types import JSONObject


@tool(
    description="Create a chat completion using OpenAI.",
    tags=["chat", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def openai_create_response(
    model: str = "gpt-4o-mini",
    messages: list[dict[str, str]] | None = None,
    system_message: str | None = None,
    temperature: float = 0.7,
    max_tokens: int = 1000,
    stream: bool = False,
) -> JSONObject:
    """Create a chat completion.

    Args:
        model: Model to use (gpt-4o, gpt-4o-mini, gpt-4-turbo, etc.).
        messages: List of message objects with role and content.
        system_message: Optional system message to prepend.
        temperature: Sampling temperature (0.0-2.0).
        max_tokens: Maximum response tokens.
        stream: Whether to stream responses.

    Returns:
        Chat completion response.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_model(model)
    validate_temperature(temperature)
    validate_max_tokens(max_tokens)

    if messages is None:
        messages = []
    else:
        for msg in messages:
            if "content" in msg:
                validate_message_content(msg["content"])

    if system_message:
        messages = [{"role": "system", "content": system_message}] + messages

    body: JSONObject = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": stream,
    }

    result = await request(HttpMethod.POST, "/chat/completions", body)
    return result


chat_tools = [openai_create_response]