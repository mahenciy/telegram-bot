from telegram.ext import Updater, CommandHandler
import random
import datetime
import requests

# === ТВОЙ ТОКЕН БОТА СЮДА ===
TOKEN = "7667501486:AAF8gkKTV068uZEfiX18dqDxLTr7vGFqzzQ"

# 🎱 Магические ответы
MAGIC_ANSWERS = [
    "Без сомнений", "Скорее всего", "Лучше не знать",
    "Возможно", "Спроси позже", "Не рассчитывай на это",
    "Да!", "Нет!", "Очень вероятно", "Сомневаюсь"
]

# 😂 Шутки
JOKES = [
    "Почему программисты не летают? Потому что они багнутые.",
    "Что говорит Python, когда его забыли импортировать? 'import me, maybe?'",
    "Как называется кот-программист? Scratch!",
    "Сегментационная ошибка — это когда память ушла, но обещала вернуться.",
]

def start(update, context):
    update.message.reply_text("Привет! Я прикольный бот 🤖. Вот, что я умею:\n"
                              "/day — Какой сегодня день?\n"
                              "/joke — Хочу шутку!\n"
                              "/8ball <вопрос> — Магический шар\n"
                              "/dice — Бросить кубик\n"
                              "/cat — Прислать кота 🐱")

def day(update, context):
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    update.message.reply_text(f"Сегодня: {today}")

def joke(update, context):
    update.message.reply_text(random.choice(JOKES))

def eight_ball(update, context):
    if context.args:
        question = ' '.join(context.args)
        answer = random.choice(MAGIC_ANSWERS)
        update.message.reply_text(f"🔮 Ты спросил: {question}\nОтвет: {answer}")
    else:
        update.message.reply_text("❓ Ты должен задать вопрос. Пример:\n/8ball Буду ли я богат?")

def dice(update, context):
    roll = random.randint(1, 6)
    update.message.reply_text(f"🎲 Ты бросил кубик: {roll}")

def cat(update, context):
    try:
        response = requests.get("https://cataas.com/cat?json=true")
        data = response.json()
        cat_url = f"https://cataas.com{data['url']}"
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=cat_url)
    except Exception as e:
        update.message.reply_text("😿 Не удалось получить кота. Попробуй позже.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Команды
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("day", day))
    dp.add_handler(CommandHandler("joke", joke))
    dp.add_handler(CommandHandler("8ball", eight_ball))
    dp.add_handler(CommandHandler("dice", dice))
    dp.add_handler(CommandHandler("cat", cat))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
