# Email ↔ Telegram AI Agent

An AI-powered assistant that:
- Reads Gmail messages (Primary inbox only) 📧
- Summarizes them using an LLM (LangChain + Mistral) 🤖
- Forwards summaries to Telegram 📲
- Lets you reply with shorthand on Telegram, expands it into a professional email, and replies in the same Gmail thread 🔄

## 🚀 Features
- Gmail API integration (read + threaded replies)
- Telegram Bot API integration
- LangChain-based summarization + reply generation
- Async architecture with Python
- Works with Hugging Face API or local models (Ollama / Transformers)

## 🛠 Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/email-telegram-ai-agent.git
   cd email-telegram-ai-agent
