# OpenAI MCP Server

A Type 3 DAuth MCP server for [OpenAI API](https://platform.openai.com). Provides chat completions, embeddings, moderation, and file management.

## Features

- **List Models** — View all available OpenAI models
- **Create Response** — Chat completions with GPT models
- **Create Embedding** — Text vectorization for semantic search
- **Moderate Text** — Content safety checking
- **List Files** — View uploaded files
- **Upload File** — Upload files for fine-tuning or assistants

## Authentication

This server uses **Type 3 DAuth** (Dedalus Auth) — your API key is encrypted client-side and decrypted in a secure Dedalus enclave.

### Get Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Create a new secret key
3. Copy the key

## Installation

```bash
git clone https://github.com/dedalus-labs/openai-mcp.git
cd openai-mcp
pip install -e .
cp .env.example .env
# Edit .env and add OPENAI_API_KEY
```

## Available Tools

### `openai_list_models`

List all available OpenAI models.

```python
openai_list_models()
```

### `openai_create_response`

Create a chat completion.

```python
openai_create_response(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello!"}],
    temperature=0.7,
    max_tokens=500,
)
```

### `openai_create_embedding`

Generate text embeddings.

```python
openai_create_embedding(
    input="The quick brown fox",
    model="text-embedding-3-small",
)
```

### `openai_moderate_text`

Check content for harmful material.

```python
openai_moderate_text(input="This is a test message")
```

### `openai_list_files`

List uploaded files.

```python
openai_list_files(purpose="assistants", limit=50)
```

### `openai_upload_file`

Upload a file.

```python
openai_upload_file(file_path="/path/to/file.jsonl", purpose="batch")
```

## Cost & Rate Limits

OpenAI uses pay-per-token pricing. Check https://openai.com/pricing for current rates.

## Deploy to Dedalus

1. Push to GitHub (public repo)
2. Go to https://www.dedaluslabs.ai/dashboard
3. Add Server → Connect GitHub repo
4. Set `OPENAI_API_KEY` as Required Credential
5. Deploy

## License

MIT