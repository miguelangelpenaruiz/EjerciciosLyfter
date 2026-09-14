import random

secret_number = random.randint(1,10)

user_guess = int(input("Choose a number between 1 and 10: \n"))

while user_guess != secret_number:
    user_guess = int(input("Choose a number between 1 and 10: \n"))

print(f"Yes! the secret number is {secret_number}")
#
