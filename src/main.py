# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""OpenAI MCP Server - Main Entry Point."""

from __future__ import annotations

import os

from dotenv import load_dotenv

from dedalus_mcp import MCPServer
from dedalus_mcp.server import TransportSecuritySettings

from openai import create_openai_connection, openai_tools

load_dotenv()


def create_server() -> MCPServer:
    """Create and configure the OpenAI MCP server.

    Returns:
        Configured MCPServer instance.

    """
    openai_conn = create_openai_connection()

    server = MCPServer(
        name="openai-mcp",
        connections=[openai_conn],
        http_security=TransportSecuritySettings(
            enable_dns_rebinding_protection=False
        ),
        streamable_http_stateless=True,
        authorization_server=os.getenv(
            "DEDALUS_AS_URL", "https://as.dedaluslabs.ai"
        ),
    )

    server.collect(*openai_tools)

    return server


async def main() -> None:
    """Start the server."""
    server = create_server()
    await server.serve(port=8080)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())