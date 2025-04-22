def read_passwords(file_path):
    try:
        with open(file_path, 'r') as file:
            passwords = file.readlines()
            passwords = [password.strip() for password in passwords]  # Remove newline characters
            return passwords
    except FileNotFoundError:
        print("File not found.")
        return []

file_path = "codes.txt"  # Path to your text file containing passwords
passwords_list = read_passwords(file_path)

