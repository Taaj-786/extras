import requests
import time
import random
import string


def send_Req(code, cookie):
    session = requests.Session()
    cookie = {'sab': cookie}
    session.cookies.update(cookie)

    code_url = "https://utcrgb.com/home/redeem"
    payload = {'uniqueCode': code}

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://utcrgb.com/home/redeem',
        'Upgrade-Insecure-Requests': '1'
    }

    response = session.post(code_url, data=payload, headers=headers)

    return response


def generate_code():
    characters = string.ascii_uppercase + string.digits  # Uppercase letters + digits
    code = ''.join(random.choices(characters,
                                  k=8))  # Generate an 8-character code
    return code


def main(cookie):
    while True:
        code = generate_code()
        response = send_Req(code, cookie)
        print(response.text, code)

        time.sleep(5)  # Wait for 5 seconds before generating the next code


cookie = "ur cookie"
code = "ur code"
send_Req(code , cookie)
print("done")