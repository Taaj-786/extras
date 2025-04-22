import requests
import time

token = "ur token"

channel_id = ""


def sendMsg(message, channel_id, token):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Authorization': token
}

    json_data = {
    'content': message
}

    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",     headers=headers, json=json_data)
    
    
    
for i in range(1, 50):
    message = f"RPG love buy adventure cooldown"
    m2 = 'RPG adv h'
    sendMsg(message, channel_id, token)
    time.sleep(1)
    sendMsg(m2, channel_id, token)
    print(i)

    i =+1
    time.sleep(2)
    
