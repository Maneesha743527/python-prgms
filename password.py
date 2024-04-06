import random
import string

class PasswordGenerator:
    def __init__(self):
        self.all_characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self, length):
        password = ''.join(random.choice(self.all_characters) for _ in range(length))
        return password

password_generator = PasswordGenerator()
desired_length = int(input("Enter the desired length of the password: "))
password = password_generator.generate_password(desired_length)
print("Generated password:", password)
