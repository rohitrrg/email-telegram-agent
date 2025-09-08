from telegram import Bot
import asyncio


BOT_TOKEN = open("config/telegram_token.txt").read().strip()
CHAT_ID = "809102927"   # replace with your ID

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="🚀 Test message from your Email Agent bot!")

if __name__ == "__main__":
    asyncio.run(main())