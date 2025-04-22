import requests
import time

def send_Req(code, tok):
    session = requests.Session()
    cookie = {'sab':tok}
    session.cookies.update(cookie)


    code_url = "https://utcrgb.com/home/redeem"
    payload = {'uniqueCode': code}
    

    headers = {                                                                                                                                                                                                                                                            
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://utcrgb.com/home/redeem',
        'Upgrade-Insecure-Requests': '1'
    }

    response = session.post(code_url, data=payload, headers=headers)

    print(response)



def read_passwords(file_path):
    try:
        with open(file_path, 'r') as file:
            passwords = file.readlines()
            passwords = [password.strip() for password in passwords]  # Remove newline characters
            return passwords
    except FileNotFoundError:
        print("File not found.")
        return []

file_path = "codes.txt"  # Path to your text file containing password
list = read_passwords(file_path)


tokens = ["uu7gqpms336ler7vmoki9tbnjikrfs6k"]
codes = list

for tok in tokens:
    for i in range(5):
        if codes:
            code = codes.pop(0)
            send_Req(code, tok)
            print(f"{tok} {code}")