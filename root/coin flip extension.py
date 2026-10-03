import random
strike = 0
while True:
    coin = random.choice(["heads", "tails"])
    while True:
        guess = (input("Enter your guess: heads or tails?")).lower().strip()
        if guess == "heads" or guess == "tails":
            break
        else:
            print("Invalid input")
    if guess == coin:
        print("Correct")
        strike = 0
    else:
        print("Incorrect")
        strike = strike + 1
    if strike == 3:
        print("You have hit three strikes. Game Over!")
        break





