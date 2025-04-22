import requests
import time
import schedule

token = "yout token"

channel_id = "ch id"


def sendMsg(message, channel_id, token):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Authorization': token
}

    json_data = {
    'content': message
}

    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",     headers=headers, json=json_data)
    


def hunt():
        m = 'RPG Hunt H T'
        sendMsg(m, channel_id, token)
        print('Hunt Done')

def work(cmd):
    m = f'RPG {cmd}'
    sendMsg(m, channel_id, token)
    print(cmd, 'Done')
    
def farm(item):
    m = f'RPG Farm {item}'
    sendMsg(m, channel_id, token)
    print('Farmed', item)

schedule.every(1).minutes.do(hunt)
schedule.every(5).minutes.do(work, 'Dynamite')
schedule.every(10).minutes.do(farm, 'Carrot')

while True:
    schedule.run_pending()
    time.sleep(0.5)