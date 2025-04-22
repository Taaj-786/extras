import requests
import time

token = "your token....."

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
    
def read():
    file_path = "/storage/emulated/0/run/status.txt"
    with open(file_path, "r") as file:
        text = file.read()
        return int(text)
        
def write(new_content):
    file_path = "/storage/emulated/0/run/status.txt"
    with open(file_path, "w") as file:
        file.write(new_content)
        

def main(end):
    
    while True:
        s=(read()+1)
        if s>end:
            print(f"Already done {s-1}")
            break
            
        #message = f"RPG love share <@id..>"
        #message = f"RPG love share <@id,,> {s}/50 Extras"
        m2 = 'RPG Hunt H T'
        
       # sendMsg(message, channel_id, token)
      #  time.sleep(0.5)
        sendMsg(m2, channel_id, token)

        write(str(s))
        print("No. ", s)
        time.sleep(60.3)
        
#write("0")
main(1000)