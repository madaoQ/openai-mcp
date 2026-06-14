# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Moderation tools for OpenAI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from openai.guards import validate_message_content
from openai.request import request
from openai.types import JSONObject


@tool(
    description="Check text for potentially harmful content.",
    tags=["moderate", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def openai_moderate_text(
    input: str | list[str],
) -> JSONObject:
    """Moderate text for harmful content.

    Args:
        input: Text or list of texts to moderate.

    Returns:
        Moderation results with flagged categories.

    Raises:
        ValueError: If input is invalid.
        RuntimeError: If the API request fails.

    """
    if isinstance(input, str):
        validate_message_content(input)
    elif isinstance(input, list):
        if not input:
            raise ValueError("Input list cannot be empty")
        for item in input:
            validate_message_content(item)

    body: JSONObject = {"input": input}
    result = await request(HttpMethod.POST, "/moderations", body)
    return result


moderate_tools = [openai_moderate_text]