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
   git clone https://github.com/rohitrrg/email-telegram-agent.git
   cd email-telegram-agent

2. Install Dependencies
   ```bash
   pip install -r requirements.txt

3. Add config files
   *  config/gmail_credentials.json (downloaded from Google Cloud)
   *  config/telegram_token.txt (from BotFather)
   *  Run quickstart once to generate token.json

4. Run the App
   ```bash
   python src/main.py

## Example Flow
1. New Gmail → Telegram Summary:
   ```bash
   📧 Subject: Project Report Submission

   Summary: Priya reminded Rohit to submit the report by Feb 12, including progress and next plans.

2. Reply on Telegram
   ```bash
   will send tomorrow

3. Gmail reply sent:
   ```bash
   Dear Priya,

   Thank you for the reminder. I will submit the report tomorrow.

   Best regards,
   Rohit

## ⚡ Tech Stack
- Python

- Gmail API

- Telegram Bot API

* LangChain

* Hugging Face
