import os
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7667501486:AAF8gkKTV068uZEfiX18dqDxLTr7vGFqzzQ'  # Замени на свой токен

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот. Напиши /restart, чтобы перезапустить меня.")

# Команда /restart
async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Перезапускаюсь...")
    # Перезапуск текущего скрипта
    os.execv(sys.executable, ['python'] + sys.argv)

# Основной блок
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("restart", restart))

app.run_polling()
#Test
