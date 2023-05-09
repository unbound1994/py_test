import requests

from read_env import read_env


read_env("../.env")


def getUpdates():
    TOKEN = '6176689920:AAGkjr-ahrQLcnVUKs4DzVyq8MG0b4W1LaU'
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    return requests.get(url).json()


def sendMessage(message, chat_id):
    TOKEN = '6176689920:AAGkjr-ahrQLcnVUKs4DzVyq8MG0b4W1LaU'
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()


