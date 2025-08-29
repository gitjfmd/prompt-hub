# 🧠 Full-Prompt-Hub

<div align="center">

**The Ultimate Collection of AI System Prompts**

*A comprehensive, structured, and community-curated repository of AI prompts from top sources*

[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/full-prompt-hub?style=social)](https://github.com/YOUR_USERNAME/full-prompt-hub/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/full-prompt-hub?style=social)](https://github.com/YOUR_USERNAME/full-prompt-hub/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[🚀 Quick Start](#-quick-start) • [📁 Browse Prompts](#-repository-structure) • [🤝 Contributing](#-contributing) • [📖 Documentation](#-documentation)

</div>

---

## 🎯 What is Full-Prompt-Hub?

Full-Prompt-Hub is the **largest open-source collection** of AI system prompts, consolidating the best prompts from across the internet into a single, well-organized repository. Whether you're building AI agents, engineering prompts, or researching AI behavior, this is your one-stop destination.

### ✨ Key Features

- 🔥 **1,600+ Prompts** from 70+ AI services
- 🏗️ **Triple Organization** by service, task, and type
- 📊 **Rich Metadata** for every prompt
- 🔍 **Easy Discovery** with structured navigation
- 🤝 **Community-Driven** with contribution guidelines
- 📱 **Ready for Integration** into your projects

---

## 📊 Repository Stats

| Metric | Count |
|--------|-------|
| **Total Prompts** | 1,627 |
| **AI Services** | 70+ |
| **Fabric Patterns** | 229 |
| **Source Repositories** | 7 |
| **Organization Schemes** | 3 |

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/full-prompt-hub.git
cd full-prompt-hub
```

### 2. Browse Prompts
```bash
# Browse by AI service
ls by-service/openai/
ls by-service/anthropic/

# Browse by task
ls by-task/system-prompt/
ls by-task/task-prompt/

# Browse by type
ls by-type/leaked/
ls by-type/pattern/
```

### 3. Use a Prompt
```bash
# View a specific prompt
cat by-service/openai/20250828-openai-chatgpt5-20250807.md

# Copy to clipboard (macOS)
pbcopy < by-service/openai/20250828-openai-chatgpt5-20250807.md

# Copy to clipboard (Linux)
xclip -selection clipboard < by-service/openai/20250828-openai-chatgpt5-20250807.md
```

---

## 📁 Repository Structure

```
full-prompt-hub/
├── 📂 by-service/          # Organized by AI service
│   ├── 🤖 openai/          # ChatGPT, GPT-4, DALL-E prompts
│   ├── 🧠 anthropic/       # Claude prompts
│   ├── 🔍 google/          # Gemini, Jules prompts
│   ├── ⚡ xai/             # Grok prompts
│   └── 📱 [70+ services]/  # And many more...
├── 📂 by-task/             # Organized by task type
│   ├── 🎯 system-prompt/   # Core system instructions
│   └── ⚙️ task-prompt/     # Specific task patterns
├── 📂 by-type/             # Organized by prompt type
│   ├── 🔓 leaked/          # Reverse-engineered prompts
│   ├── 🧩 pattern/         # Fabric framework patterns
│   └── 🎛️ system-prompt/   # Official system prompts
├── 📚 docs/                # Documentation
├── 🛠️ tools/              # Management scripts
└── 📖 README.md           # This file
```

---

## 🎯 Featured AI Services

<table>
<tr>
<td align="center"><strong>🤖 OpenAI</strong><br/>ChatGPT, GPT-4, DALL-E</td>
<td align="center"><strong>🧠 Anthropic</strong><br/>Claude 3.5 Sonnet, Opus</td>
<td align="center"><strong>🔍 Google</strong><br/>Gemini, Jules</td>
<td align="center"><strong>⚡ xAI</strong><br/>Grok 2, Grok 3</td>
</tr>
<tr>
<td align="center"><strong>🎨 Midjourney</strong><br/>Image generation</td>
<td align="center"><strong>💻 GitHub</strong><br/>Copilot, Copilot Chat</td>
<td align="center"><strong>🌐 Perplexity</strong><br/>Search-augmented AI</td>
<td align="center"><strong>🔧 Cursor</strong><br/>AI code editor</td>
</tr>
</table>

---

## 🧩 Fabric Patterns Collection

This repository includes **229 patterns** from the [Fabric framework](https://github.com/danielmiessler/fabric), organized by category:

- **📊 Analysis**: `analyze_answers`, `analyze_claims`, `analyze_debate`
- **✍️ Creation**: `create_story`, `write_essay`, `generate_summary`
- **🔍 Extraction**: `extract_data`, `extract_entities`, `extract_insights`
- **🎯 Specialized**: `code_review`, `threat_modeling`, `security_analysis`

---

## 📖 How to Use Prompts

### Understanding Prompt Metadata

Each prompt includes rich metadata in YAML frontmatter:

```yaml
---
uid: 20250828-openai-chatgpt5-001
name: "ChatGPT-5 System Prompt"
description: "Core system instructions for ChatGPT-5"
author: "OpenAI"
date: 2025-08-07
service: [openai, chatgpt-5]
task: [system-prompt, general-purpose]
type: [system-prompt, leaked]
source:
  - name: "leaked-system-prompts"
    url: "https://github.com/jujumilk3/leaked-system-prompts"
---
```

### Example Usage

```python
# Python example: Load and use a prompt
import yaml
import frontmatter

# Load a prompt file
with open('by-service/openai/chatgpt5-prompt.md', 'r') as f:
    post = frontmatter.load(f)
    
metadata = post.metadata
content = post.content

print(f"Using prompt: {metadata['name']}")
print(f"For service: {metadata['service']}")
print(f"Content: {content}")
```

---

## 🔍 Finding the Right Prompt

### By AI Service
Looking for prompts for a specific AI service?
```bash
# OpenAI prompts
find by-service/openai/ -name "*.md"

# Anthropic Claude prompts  
find by-service/anthropic/ -name "*.md"

# All available services
ls by-service/
```

### By Task Type
Need prompts for a specific task?
```bash
# System prompts (core instructions)
ls by-task/system-prompt/

# Task-specific patterns
ls by-task/task-prompt/
```

### By Prompt Type
Looking for specific types of prompts?
```bash
# Leaked/reverse-engineered prompts
ls by-type/leaked/

# Fabric framework patterns
ls by-type/pattern/

# Official system prompts
ls by-type/system-prompt/
```

---

## 🛠️ Tools and Scripts

The repository includes helpful tools in the `tools/` directory:

- **`consolidate_prompts.py`**: Script to merge new repositories
- **`validate_metadata.py`**: Validate prompt metadata
- **`search_prompts.py`**: Search across all prompts
- **`export_formats.py`**: Export prompts to different formats

---

## 📚 Documentation

- **[Metadata Guide](METADATA_GUIDE.md)**: Understanding prompt metadata
- **[Contributing Guide](docs/CONTRIBUTING.md)**: How to contribute
- **[Style Guide](docs/STYLE_GUIDE.md)**: Writing and formatting standards
- **[API Documentation](docs/API.md)**: Programmatic access

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🆕 Adding New Prompts
1. Fork the repository
2. Add your prompt with proper metadata
3. Follow our [style guide](docs/STYLE_GUIDE.md)
4. Submit a pull request

### 🔄 Updating Existing Prompts
1. Check for newer versions of prompts
2. Update metadata and content
3. Maintain backward compatibility

### 🐛 Reporting Issues
- Found a broken prompt? [Open an issue](https://github.com/YOUR_USERNAME/full-prompt-hub/issues)
- Have suggestions? [Start a discussion](https://github.com/YOUR_USERNAME/full-prompt-hub/discussions)

---

## 📈 Roadmap

- [ ] **Website Development**: Interactive web interface
- [ ] **API Development**: RESTful API for programmatic access
- [ ] **Search Enhancement**: Advanced search and filtering
- [ ] **Community Features**: Ratings, comments, favorites
- [ ] **Automated Updates**: Sync with source repositories
- [ ] **Mobile App**: Native mobile applications

---

## 🙏 Acknowledgments

This repository consolidates amazing work from these source repositories:

| Repository | Description | Stars |
|------------|-------------|-------|
| [awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) | Curated system prompts collection | 3.7k ⭐ |
| [fabric](https://github.com/danielmiessler/fabric) | AI augmentation framework | 33.2k ⭐ |
| [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) | Reverse-engineered prompts | - |
| [TheBigPromptLibrary](https://github.com/0xeb/TheBigPromptLibrary) | Comprehensive prompt library | - |
| [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | ChatGPT prompts collection | - |
| [LLM-System-Prompts](https://github.com/guy915/LLM-System-Prompts) | Multi-LLM system prompts | - |

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_USERNAME/full-prompt-hub&type=Date)](https://star-history.com/#YOUR_USERNAME/full-prompt-hub&Date)

---

<div align="center">

**Made with ❤️ by the AI community**

[⭐ Star this repo](https://github.com/YOUR_USERNAME/full-prompt-hub) • [🐛 Report Bug](https://github.com/YOUR_USERNAME/full-prompt-hub/issues) • [💡 Request Feature](https://github.com/YOUR_USERNAME/full-prompt-hub/issues)

</div>

