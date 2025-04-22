import requests
import time

def send_Req(code, tok):
    session = requests.Session()
    cookie = {'sab': tok}
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
    return response
    
def MAIN(stop):
    with open('codes.txt', 'r+') as file:
        lines = file.readlines()

        for tok in token:
            for _ in range(5):
                if not lines:
                    break

                code = lines[0].strip()

                check = send_Req(code, tok)

                print(check)

                if check.status_code == 200:
                    print(_+1,tok, code)

                    del lines[0]
                    file.seek(0)
                    file.writelines(lines)
                    file.truncate()
                    time.sleep(stop)
                else:
                    continue

                
                
token = ["uu7gqpms336ler7vmoki9tbnjikrfs6k", "i3lva17cqn6odfc4pmflehqdq4f3ok92", "bcaacc52e07rahhvuqc4dui0ennc6spb", "95c4ifj8g5rvpkpe4ashh6tecrb799j6", "vbtnfng6992jvl432j0oqe33chpo9oft"] 

#token = ["uu7gqpms336ler7vmoki9tbnjikrfs6k", "bcaacc52e07rahhvuqc4dui0ennc6spb", "95c4ifj8g5rvpkpe4ashh6tecrb799j6", "vbtnfng6992jvl432j0oqe33chpo9oft"] 
                
MAIN(0.01)
