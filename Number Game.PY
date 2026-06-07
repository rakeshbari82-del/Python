print("=" * 50)
print("🎮 NUMBER GUESSING GAME 🎮")
print("=" * 50)

secret = 27
attempts = 0
max_attempts = 5
won = False

while attempts < max_attempts and not won:

    guess = int(input("\nEnter Your Guess (1-50) : 1"))
    attempts += 1

    if guess == secret:
        print("\n Congratulations! You guessed the secret number!")
        won = True

    else:
        different = abs(secret - guess)

        if difference > 20:
            print("Ice Cold!")

        elif difference > 10:
            print("Cold!")

        lives_left = max_attempts - attempts
        print("Remaining Lives: ", end="")
        for i in range(live_left):
            print("lovely", end="")
        print()