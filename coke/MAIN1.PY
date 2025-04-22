import requests
import time

def send_Req(code):
    session = requests.Session()
    cookie = {'sab': '5da2g4hrv5uugdg4p92tvdjhp866a993'}
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

def delete_first_line():
    file_name = "codes1.txt"
    with open(file_name, 'r+') as file:
        first_line = file.readline().strip()
        # print(first_line)
        lines = file.readlines()  # Read all lines into a list
        file.seek(0)  # Move the file pointer to the beginning
        file.writelines(lines)  # Write all lines except the first one back to the file
        file.truncate()  # Truncate the file to remove any remaining content
        return first_line

def count_lines():
    file_name = "codes1.txt"  
    with open(file_name, 'r') as file:
        lines = file.readlines()  # Read all lines into a list
        return len(lines)  # Count the number of lines in the list

def main(time_Gap):
    while True:
        num_lines = count_lines()
        if num_lines <= 0:
            break
    
    
        code = delete_first_line()
        send_Req(code)

        time.sleep(time_Gap)



main(0)
