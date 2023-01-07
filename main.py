import requests
import json
from time import sleep

with open("config.json") as f:
  config = json.load(f)

payload = {"content": f"{config["message"]}"}
errorm = {"content'": "ERROR!"}
header = {"authorization": f"{config["TOKEN"]"}

def post():
    Angka = 1
    Angkas = 1
    for i in config["CHANNELID"]:
        if Angka > len(config["CHANNELID"]):
            Angka = 1
        if i == len(config["CHANNELID"]):
            sleep(config["DELAY"])
        else:
            url = f"https://discord.com/api/v9/channels/{i}/messages"
            urll = f"https://discord.com/api/v9/channels/{config["DONE_SEND_CHANNEL_ID"]}/messages"
            requests.post(url, headers=header, data=payload)
            sleep(2)
            ms = {'content': f'Done Send Message \n Message {Angka} / {len(config["CHANNELID"])} ({Angkas})'}
            md = f'Done Send Message \n Message {Angka} / {len(config["CHANNELID"])} ({Angkas})'
            requests.post(urll,headers=header, data=ms)
            sleep(10)
            Angka += 1
            Angkas += 1
while True:
    post()