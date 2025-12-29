import requests as rq
import time

with open("token.txt", "r") as file:
    BOT_TOKEN = file.readline().strip()

API_URL = 'https://api.telegram.org/bot'
CAT_API_URL = "https://api.thecatapi.com/v1/images/search"
TEXT = "Вижу"
ERROR_TEXT = "неработет"
MAX_COUNTER = 5

offset = -2
counter = 0
chat_id: int
cat_link: str
cat_response: rq.Response

while counter < MAX_COUNTER:
    print("attempt=", counter)
    update = rq.get(f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}").json()

    if update["result"]:
        for result in update["result"]:
            offset = result["update_id"]
            chat_id = result["message"]["from"]["id"]
            cat_response = rq.get(CAT_API_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]["url"]
                rq.get(f"{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}")
            else:
                rq.get(f"{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}")
                
    time.sleep(1)
    counter += 1