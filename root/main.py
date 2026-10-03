import random

while True:
    coin = random.choice(["heads", "tails"])
    while True:
        guess = (input("Enter your guess:"))
        if guess is "Heads" or guess is "Tails":
            break
        else:
            "Invalid input"
    if guess == coin:
        "Correct"
    else:
        "Incorrect"
