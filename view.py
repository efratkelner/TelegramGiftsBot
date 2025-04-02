import os
from flask import Flask, request
import requests
import controller
app = Flask(__name__)
app.secret_key = '1234'


@app.route("/sanity", methods=['GET'])
def index():
    """
    server home page 
    :return: str to show that the server is running
    """
    return 'Server is running'

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_INIT_WEBHOOK_URL = os.getenv("TELEGRAM_WEBHOOK_URL").format(TOKEN)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/message', methods=["POST"])
def handle_message():
    """
    get message from the telegram bot and send the wright answer
    """
    print("got message")
    answer='I dont understand :('
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


if __name__ == '__main__':
    app.run(port=5002)
