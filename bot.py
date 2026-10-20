
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("8530047129:AAGKilPDhiyy0Id1LhAY3f4CABiFi1TQ8Fs")


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "Привет! 👋\n\n"
        "Я бот колледжа ТВМК.\n"
        "Выбери команду /help, чтобы узнать, что я умею."
    )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start — запуск бота\n"
        "/help — помощь"
    )


def main():
    if not TOKEN:
        raise RuntimeError(
            "Не задана переменная TELEGRAM_BOT_TOKEN"
        )

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    logging.info("Бот запускается")
    app.run_polling()


if __name__ == "__main__":
    main()
