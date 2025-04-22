import random
import string

def generate_password():
    password = '24'
    password += ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return password

with open('codes1.txt', 'w') as file:
    for _ in range(1000):
        password = generate_password()
        file.write(password + '\n')
