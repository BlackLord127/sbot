import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = 'YOUR_BOT_TOKEN'

# Функция для преобразования текста в голосовое сообщение с использованием API от ElevenLabs
def convert_text_to_voice(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/ozWfRRyyPE3UOGamMiwD"
    payload = {
        "text": text
    }
    headers = {
        "xi-api-key": "22f131038f54d8dacf48a847516c4749",
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    voice_message = response.content
    return voice_message

# Обработчик команды /start
def start(update, context):
    update.message.reply_text('Привет! Отправь мне текст, который хочешь преобразовать в голосовое сообщение.')

# Обработчик текстовых сообщений
def text_to_voice(update, context):
    text = update.message.text
    voice_message = convert_text_to_voice(text)
    update.message.reply_voice(voice_message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, text_to_voice))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()