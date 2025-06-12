import telebot
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)

auto_mode = False

@bot.message_handler(commands=['start'])
def start(message):
    if str(message.chat.id) == ADMIN_CHAT_ID:
        bot.send_message(message.chat.id, "🤖 Bot V5 Activated!\nUse /signal to get instant signal.\nUse /auto to start auto mode.\nUse /stop to end auto.")
    else:
        bot.send_message(message.chat.id, "❌ Unauthorized access")

@bot.message_handler(commands=['signal'])
def signal(message):
    if str(message.chat.id) == ADMIN_CHAT_ID:
        send_signal(message.chat.id)

@bot.message_handler(commands=['auto'])
def auto(message):
    global auto_mode
    if str(message.chat.id) == ADMIN_CHAT_ID:
        auto_mode = True
        bot.send_message(message.chat.id, "🔁 Auto mode ON (sends every 15 seconds)...")
        while auto_mode:
            send_signal(message.chat.id)
            time.sleep(15)

@bot.message_handler(commands=['stop'])
def stop(message):
    global auto_mode
    if str(message.chat.id) == ADMIN_CHAT_ID:
        auto_mode = False
        bot.send_message(message.chat.id, "🛑 Auto mode OFF.")

def send_signal(chat_id):
    signal = "🔹 Forex Signal: BUY or SELL\nTimeframe: 1m\nAccuracy: 97%"
    bot.send_message(chat_id, signal)

bot.infinity_polling()
