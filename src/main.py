import os
import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from gmail_handler import gmail_service, check_new_email
from summarizer import summarize_email
from telegram_handler import latest_email, start, handle_response

# ============ CONFIG ============
with open("config/telegram_token.txt") as f:
    TELEGRAM_TOKEN = f.read().strip()

TELEGRAM_CHAT_ID = "809102927"  # replace with your chat ID


# Async email polling task
async def poll_emails(app):
    service = gmail_service()
    last_id = None
    while True:
        email = check_new_email(service, last_id)
        if email:
            last_id = email["id"]
            latest_email.update(email)
            summary = summarize_email(email["body"], email["subject"])
            text = (
                f"📧 New Email from {email['from']}\n"
                f"Subject: {email['subject']}\n\n"
                f"Summary: {summary}"
            )
            # ✅ await required for v20+
            await app.bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text)
        await asyncio.sleep(30)  # check every 30 sec


async def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

    # start background task for polling Gmail
    asyncio.create_task(poll_emails(app))

    print("🚀 Email ↔ Telegram Agent running...")
    await app.run_polling()


if __name__ == "__main__":
    import nest_asyncio
    import asyncio

    nest_asyncio.apply()  # allows re-using a running loop
    asyncio.get_event_loop().run_until_complete(main())