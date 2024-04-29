import telebot
from telebot import types
from googletrans import Translator
import random

API_TOKEN = '7019669863:AAGDpWYmnYQkhPvjyCBhxeohmLurNNcGvcI'

bot = telebot.TeleBot(API_TOKEN)
translator = Translator()

translation_history = {}
user_settings = {}
guessing_games = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    translate_button = types.KeyboardButton('📝 Перевести текст')
    history_button = types.KeyboardButton('📚 История переводов')
    reminder_button = types.KeyboardButton('⏰ Напоминания')
    guess_number_button = types.KeyboardButton('🔢 Угадай число')
    markup.add(translate_button, history_button, reminder_button, guess_number_button)
    
    bot.reply_to(message, "Привет! Я бот-переводчик и ассистент. Выбери опцию для продолжения:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '📝 Перевести текст')
def handle_translate_prompt(message):
    bot.reply_to(message, "Отправь мне текст, который нужно перевести.")

@bot.message_handler(func=lambda message: message.text == '📚 История переводов')
def handle_history(message):
    user_id = message.chat.id
    
    if user_id in translation_history:
        history = translation_history[user_id]
        history_text = '\n'.join([f"{original} -> {translated}" for original, translated in history])
        bot.reply_to(message, f"История переводов:\n{history_text}")
    else:
        bot.reply_to(message, "У вас пока нет истории переводов.")

@bot.message_handler(func=lambda message: message.text == '⏰ Напоминания')
def handle_reminders(message):
    user_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(row_width=1)
    add_reminder_button = types.KeyboardButton('Добавить напоминание')
    view_reminders_button = types.KeyboardButton('Посмотреть напоминания')
    markup.add(add_reminder_button, view_reminders_button)
    bot.reply_to(message, "Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Добавить напоминание')
def handle_add_reminder_prompt(message):
    user_id = message.chat.id
    user_settings[user_id] = user_settings.get(user_id, {})
    user_settings[user_id]['adding_reminder'] = True
    bot.reply_to(message, "Введите текст напоминания:")

@bot.message_handler(func=lambda message: user_settings.get(message.chat.id, {}).get('adding_reminder', False))
def handle_add_reminder(message):
    user_id = message.chat.id
    user_settings[user_id]['adding_reminder'] = False
    if 'reminders' not in user_settings[user_id]:
        user_settings[user_id]['reminders'] = []
    user_settings[user_id]['reminders'].append(message.text)
    bot.reply_to(message, "Напоминание добавлено.")

@bot.message_handler(func=lambda message: message.text == 'Посмотреть напоминания')
def handle_view_reminders(message):
    user_id = message.chat.id
    reminders = user_settings.get(user_id, {}).get('reminders', [])
    
    if reminders:
        reminders_text = '\n'.join([f"{idx + 1}. {reminder}" for idx, reminder in enumerate(reminders)])
        bot.reply_to(message, f"Ваши напоминания:\n{reminders_text}")
    else:
        bot.reply_to(message, "У вас пока нет напоминаний.")

@bot.message_handler(func=lambda message: message.text == '🔢 Угадай число')
def handle_guess_number_prompt(message):
    user_id = message.chat.id
    guessing_games[user_id] = {
        'number': random.randint(1, 100),
        'attempts': 0
    }
    bot.reply_to(message, "Я загадал число от 1 до 100. Попробуй угадать!")

@bot.message_handler(func=lambda message: message.chat.id in guessing_games)
def handle_guess_number(message):
    user_id = message.chat.id
    game = guessing_games[user_id]
    
    try:
        guess = int(message.text)
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите число.")
        return
    
    game['attempts'] += 1
    
    if guess == game['number']:
        bot.reply_to(message, f"Поздравляю! Ты угадал число {game['number']} за {game['attempts']} попыток!")
        del guessing_games[user_id]  
    elif guess < game['number']:
        bot.reply_to(message, "Мое число больше.")
    else:
        bot.reply_to(message, "Мое число меньше.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    user_text = message.text
    
    translation = translator.translate(user_text, dest='en')
    translated_text = translation.text
    
    bot.reply_to(message, translated_text)
    
    if user_id not in translation_history:
        translation_history[user_id] = []
    translation_history[user_id].append((user_text, translated_text))

if __name__ == '__main__':
    bot.polling()
