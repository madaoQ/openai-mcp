# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Direct API testing client for OpenAI MCP.

This module is used for local testing without going through the MCP server.
"""

from __future__ import annotations

import asyncio
import os

import httpx
from dotenv import load_dotenv

load_dotenv()


async def test_list_models() -> None:
    """Test list_models endpoint."""
    print("Testing openai_list_models...")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment")
        return

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://api.openai.com/v1/models",
            headers=headers,
            timeout=30,
        )

    if resp.status_code == 200:
        data = resp.json()
        print(f"✓ List models successful")
        print(f"  Total models: {len(data.get('data', []))}")
    else:
        print(f"✗ Error {resp.status_code}: {resp.text[:200]}")


async def test_create_response() -> None:
    """Test create_response endpoint."""
    print("\nTesting openai_create_response...")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found")
        return

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    body = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "Say hello in one word"}],
        "max_tokens": 10,
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=body,
            timeout=30,
        )

    if resp.status_code == 200:
        data = resp.json()
        print(f"✓ Create response successful")
        choices = data.get("choices", [])
        if choices:
            msg = choices[0].get("message", {})
            print(f"  Response: {msg.get('content', 'N/A')}")
    else:
        print(f"✗ Error {resp.status_code}: {resp.text[:200]}")


async def main() -> None:
    """Run all direct API tests."""
    print("=" * 50)
    print("OpenAI Direct API Tests")
    print("=" * 50)
    print()

    await test_list_models()
    await test_create_response()

    print()
    print("=" * 50)
    print("Tests completed!")


if __name__ == "__main__":
    asyncio.run(main())