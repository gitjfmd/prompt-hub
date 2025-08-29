# Metadata Guide

Each prompt in this repository must include a YAML frontmatter block with the following metadata fields:

## Required Fields

- `uid`: A unique identifier for the prompt. Format: `YYYYMMDD-service-name-NNN`
- `name`: The name of the prompt.
- `description`: A brief description of the prompt.
- `author`: The author of the prompt.
- `date`: The date the prompt was created or last updated.
- `service`: A list of the AI services the prompt is designed for.
- `task`: A list of the tasks the prompt performs.
- `type`: A list of the types of prompt.
- `source`: A list of the sources the prompt was taken from.

## Optional Fields

- `tags`: A list of relevant tags.

## Example

```yaml
---
# METADATA (Required)
uid: 20250829-openai-chatgpt5-001
name: "ChatGPT-5 System Prompt (2025-08-07)"
description: "Leaked system prompt for ChatGPT-5 from August 7, 2025."
author: "OpenAI (leaked)"
date: 2025-08-07

# CLASSIFICATION (Required)
service:
  - openai
  - chatgpt-5
task:
  - system-prompt
  - general-purpose
type:
  - system-prompt
  - leaked

# TAGS (Optional)
- agentic
- multimodal
- safety-aligned

# SOURCE (Required)
- name: "leaked-system-prompts"
  url: "https://github.com/jujumilk3/leaked-system-prompts"
  file: "openai-chatgpt5_20250807.md"
---
```


