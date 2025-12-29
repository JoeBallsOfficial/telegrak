import requests as rq
import time

with open("token.txt", "r") as file:
    BOT_TOKEN = file.readline().strip()

offset = -2
timeout = 60
API_URL = "https://api.telegram.org/bot"
updates: dict

def do_smth() -> None:
    print("АПДЕТЬ")

while True:
    start_time = time.time()
    updates = rq.get(f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}").json()

    if updates['result']:
        for result in updates["result"]:
            offset = result["update_id"]
            do_smth()
    
    end_time = time.time()
    print(f"между апдетами {end_time - start_time}")
