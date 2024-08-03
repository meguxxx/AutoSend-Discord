import requests as req
import json
from time import sleep

with open("config.json") as f:
  config = json.load(f)

if config["TOKEN"] == "" and config["MESSAGE"] == "":
    raise Exception("TOKEN And MESSAGE Not Found")


header = {"authorization": f"{config["TOKEN"]}"}


def post():
    n = 1
    for i in config["CHANNELID"]:
        if n > len(config["CHANNELID"]):
            n = 1
        if i == len(config["CHANNELID"]):
            sleep(config["DELAY"])
            
        else:
            req.post(f"https://discord.com/api/v9/channels/{i}/messages",
                     headers=header,
                     data={'content': f"{config["MESSAGE"]}"})
            sleep(2)

            req.post(f"https://discord.com/api/v9/channels/{config["OWN_CHANNEL_ID"]}/messages",
                     headers=header,
                     data={
                            'content': f'Done Send Message \n Message {n} / {len(config["CHANNELID"])}'
                         })
            sleep(10)
            n += 1

if __name__ == "__main__":
    while True:
        post()
        