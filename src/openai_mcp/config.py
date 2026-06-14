# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""OpenAI API configuration."""

from dedalus_mcp.auth import Connection, SecretKeys

# OpenAI API base URL
OPENAI_API_BASE = "https://api.openai.com/v1"


def create_openai_connection() -> Connection:
    """Create a DAuth connection to OpenAI API.

    Uses Bearer token authentication.
    The API key is encrypted client-side and decrypted in the Dedalus enclave.

    Returns:
        Configured Connection for OpenAI API.

    """
    return Connection(
        name="openai",
        secrets=SecretKeys(token="OPENAI_API_KEY"),
        base_url=OPENAI_API_BASE,
        auth_header_format="Bearer {api_key}",
    )