import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7667501486:AAF8gkKTV068uZEfiX18dqDxLTr7vGFqzzQ"

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я крутой бот 🤖. Напиши /help чтобы узнать, что я умею!")

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start — Запуск\n"
        "/help — Помощь\n"
        "/fun — Случайный факт\n"
        "/echo <текст> — Повторю за тобой"
    )

# /echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        await update.message.reply_text(" ".join(context.args))
    else:
        await update.message.reply_text("Надо что-то написать после /echo 🤔")

# /fun
async def fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    facts = [
        "🐶 Собаки умеют чувствовать время!",
        "🚀 Первый человек в космосе — Юрий Гагарин.",
        "🧠 Мозг человека работает даже во сне.",
        "🍌 Бананы — это ягоды. А клубника — нет!",
        "🪐 Один день на Венере дольше, чем год."
    ]
    import random
    await update.message.reply_text(random.choice(facts))

# Запуск бота
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("fun", fun))

    print("Бот запущен...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
