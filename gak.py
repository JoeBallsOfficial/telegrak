import requests as rq
import time

with open("token.txt", "r") as file:
    BOT_TOKEN = file.readline().strip()

API_URL = 'https://api.telegram.org/bot'
TEXT = "Вижу"
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:
    update = rq.get(f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}").json()

    if update["result"]:
        for result in update["result"]:
            offset = result["update_id"]
            chat_id = result["message"]["from"]["id"]
            rq.get(f"{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}")
    
    time.sleep(1)
    counter += 1