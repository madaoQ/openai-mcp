# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Input validation for OpenAI API parameters."""

from __future__ import annotations

import re


# OpenAI model names: alphanumeric, hyphens, underscores, dots, slashes
_MODEL_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_./-]*$")


def validate_model(model: str) -> None:
    """Validate an OpenAI model name."""
    if not model or not _MODEL_RE.match(model):
        msg = f"Invalid model name: {model!r}"
        raise ValueError(msg)


def validate_temperature(temperature: float) -> None:
    """Validate temperature parameter."""
    if not 0.0 <= temperature <= 2.0:
        msg = f"Temperature must be between 0.0 and 2.0, got {temperature}"
        raise ValueError(msg)


def validate_max_tokens(max_tokens: int) -> None:
    """Validate max_tokens parameter."""
    if max_tokens < 1:
        msg = f"max_tokens must be at least 1, got {max_tokens}"
        raise ValueError(msg)


def validate_message_content(content: str) -> None:
    """Validate message content."""
    if not content or not content.strip():
        msg = "Message content cannot be empty"
        raise ValueError(msg)


def validate_encoding_format(format: str) -> None:
    """Validate encoding format."""
    valid_formats = {"float", "base64"}
    if format not in valid_formats:
        msg = f"encoding_format must be one of {valid_formats}, got {format}"
        raise ValueError(msg)


def validate_purpose(purpose: str) -> None:
    """Validate file purpose."""
    valid_purposes = {"assistants", "batch", "fine-tune", "vision", "user_data"}
    if purpose not in valid_purposes:
        msg = f"purpose must be one of {valid_purposes}, got {purpose}"
        raise ValueError(msg)