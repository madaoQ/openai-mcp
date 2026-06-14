# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Embedding tools for OpenAI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from openai_mcp.guards import validate_encoding_format, validate_message_content, validate_model
from openai_mcp.request import request
from openai_mcp.types import JSONObject


@tool(
    description="Create text embeddings using OpenAI.",
    tags=["embed", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def openai_create_embedding(
    input: str | list[str],
    model: str = "text-embedding-3-small",
    encoding_format: str = "float",
) -> JSONObject:
    """Create embeddings for text.

    Args:
        input: Text or list of texts to embed.
        model: Embedding model (text-embedding-3-small, text-embedding-3-large, etc.).
        encoding_format: Output format (float, base64).

    Returns:
        Embeddings response with vectors.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_model(model)
    validate_encoding_format(encoding_format)

    if isinstance(input, str):
        validate_message_content(input)
    elif isinstance(input, list):
        if not input:
            raise ValueError("Input list cannot be empty")
        for item in input:
            validate_message_content(item)

    body: JSONObject = {
        "input": input,
        "model": model,
        "encoding_format": encoding_format,
    }

    result = await request(HttpMethod.POST, "/embeddings", body)
    return result


embed_tools = [openai_create_embedding]