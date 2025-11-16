from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from reply_generator import generate_reply
from gmail_handler import gmail_service, send_email_reply


# Store latest email globally
latest_email = {"id": None, "from": None, "subject": None, "body": None}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Email Assistant started. Waiting for emails...")

async def handle_response(update, context):
    global latest_email
    shorthand = update.message.text

    if not latest_email.get("id"):
        await update.message.reply_text("⚠️ No new email to reply to yet.")
        return

    reply_text = generate_reply(latest_email['body'], shorthand)
    await update.message.reply_text("📨 Sending reply:\n\n" + reply_text)

    service = gmail_service()
    send_email_reply(
        service,
        latest_email["from"],
        latest_email["subject"],
        reply_text,
        thread_id=latest_email.get("threadId"),
        message_id=latest_email.get("message_id")
    )