import requests
import telebot


def city(update,context):
  list_of_cities = ['Erode','Coimbatore','London', 'Thunder Bay', 'California']
  button_list = []
  for each in list_of_cities:
     button_list.append(telebot.TeleBot.InlineKeyboardButton(each, callback_data = each))
  reply_markup=telebot.TeleBotInlineKeyboardMarkup(build_menu(button_list,n_cols=1)) #n_cols = 1 is for single column and mutliple rows
  requests.send_message(chat_id=update.message.chat_id, text='Choose from the following',reply_markup=reply_markup)


def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
  menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu




from flask import Flask, request
import requests
from telebot import types
import ast
import time
import controller
import telebot
import telegram

app = Flask(__name__)
app.secret_key = '1234'


@app.route("/sanity", methods=['GET'])
def index():
    """
    server home page
    :return: str to show that the server is running
    """
    return 'Server is running'


TOKEN = '1994894709:AAEgj5TTO3K8jAEQxTvc5Hms7IKLl_X0L4w'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://a52b2e6262cf.ngrok.io/message'.format(
    TOKEN)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)

string_list = {"Name": "John", "Language": "Python", "API": "pyTelegramBotAPI"}
crossIcon = u"\u274C"


def make_keyboard():
    markup = types.InlineKeyboardMarkup()
    for key, value in string_list.items():
        markup.add(types.InlineKeyboardButton(text=value,
                                              callback_data="['value', '" + value + "', '" + key + "']"),
                   types.InlineKeyboardButton(text=crossIcon,
                                              callback_data="['key', '" + key + "']"))
    return markup


@app.route('/message', methods=["POST"])
def handle_message():
    """
    get message from the telegram bot and send the wright answer
    """
    print("got message")
    answer = 'Hi! Welcome to GiftFit :)'
    command = list(request.get_json()['message']['text'].split(" "))
    if command[0] == '/prime' and len(command) == 2:
        answer = controller.is_prime(command[1])
    if command[0] == '/factorial' and len(command) == 2:
        answer = controller.is_factorial(command[1])
    if command[0] == '/palindrome' and len(command) == 2:
        answer = controller.is_palindrome(command[1])
    if command[0] == '/sqrt' and len(command) == 2:
        answer = controller.is_sqrt(command[1])
    if command[0] == '/popular':
        answer = controller.popular()
    chat_id = request.get_json()['message']['chat']['id']
    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                       .format(TOKEN, chat_id, answer))
    return "success"


@requests.message_handler(commands=['test'])
def handle_command_adminwindow(message):
    requests.send_message(chat_id=message.chat.id,
                          text="Here are the values of stringList",
                          reply_markup=make_keyboard(),
                          parse_mode='HTML')


@requests.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data.startswith("['value'"):
        print(f"call.data : {call.data} , type : {type(call.data)}")
        print(
            f"ast.literal_eval(call.data) : {ast.literal_eval(call.data)} , type : {type(ast.literal_eval(call.data))}")
        valueFromCallBack = ast.literal_eval(call.data)[1]
        keyFromCallBack = ast.literal_eval(call.data)[2]
        requests.answer_callback_query(callback_query_id=call.id,
                                       show_alert=True,
                                       text="You Clicked " + valueFromCallBack + " and key is " + keyFromCallBack)

    if call.data.startswith("['key'"):
        keyFromCallBack = ast.literal_eval(call.data)[1]
        del string_list[keyFromCallBack]
        requests.edit_message_text(chat_id=call.message.chat.id,
                                   text="Here are the values of stringList",
                                   message_id=call.message.message_id,
                                   reply_markup=make_keyboard(),
                                   parse_mode='HTML')


def city(update, context):
    genders = ['Female', 'Male']
    button_list = []
    for each in genders:
        button_list.append(types.InlineKeyboardButton(each, callback_data=each))
    reply_markup = types.InlineKeyboardMarkup(
        build_menu(button_list, n_cols=1))  # n_cols = 1 is for single column and mutliple rows
    requests.send_message(chat_id=update.message.chat_id, text='Choose from the following', reply_markup=reply_markup)


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


if __name__ == '__main__':
    app.run(port=5002)
