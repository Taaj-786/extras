import requests
import time


token = "yout token"
channel_id = "ur channel id"


def sendMsg(message, channel_id, token):
    headers = {
    'Authorization': token
}

    json_data = {
    'content': message
}

    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",headers=headers,json=json_data)
    print(response.status_code)


while True:
    # sendMsg("RPG Hunt", channel_id, token)
    # time.sleep(61)
    sendMsg("RPG slots 1m", channel_id, token)
    time.sleep(2)
  