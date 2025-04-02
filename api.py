import requests
import view

women_dict = {}
men_dict = {}


def insert(gender):
    url = "https://amazon24.p.rapidapi.com/api/product"

    querystring = {"keyword": gender, "country": "US", "page": "1"}

    headers = {
        'x-rapidapi-key': "5a487db749msh4eec802c6020d5ep18ce7ejsn5ff4cf707d21",
        'x-rapidapi-host': "amazon24.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    if gender == "women":
        for item in response["docs"]:
            if item["app_sale_price"] is not None:
                women_dict[item["app_sale_price"]] = [item["product_detail_url"], item["product_main_image_url"]]
    else:
        for item in response["docs"]:
            if item["app_sale_price"] is not None:
                men_dict[item["app_sale_price"]] = [item["product_detail_url"], item["product_main_image_url"]]


insert("men")
insert("women")
print(women_dict)
print(men_dict)





def gender(update, context):
    genders = ['Female', 'Male']
    button_list = []
    for each in genders:
        button_list.append(telebot.TeleBot.InlineKeyboardButton(each, callback_data=each))
    reply_markup = telebot.TeleBot.InlineKeyboardMarkup(
        build_menu(button_list, n_cols=1))  # n_cols = 1 is for single column and mutliple rows
    requests.send_message(chat_id=update.message.chat_id, text='Choose from the following', reply_markup=reply_markup)


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
    
    
        dict = {"Name": "John", "Language": "Python", "API": "pyTelegramBotAPI"}

    buttons = []

    for key, value in dict.items():
        buttons.append(
            [telegram.InlineKeyboardButton(text=key, url='google.com')]
        )
    keyboard = telegram.InlineKeyboardMarkup(buttons)
    chat_id = request.get_json()['message']['chat']['id']


