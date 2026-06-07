print("=" * 50)
print("🎮 NUMBER GUESSING GAME 🎮")
print("=" * 50)

secret = 27      # Secret number
attempts = 0
max_attempts = 5
won = False

while attempts < max_attempts and not won:

    guess = int(input("\nEnter your guess (1-50): "))
    attempts += 1

    if guess == secret:
        print("\n🎉 Congratulations! You guessed the secret number!")
        won = True

    else:
        difference = abs(secret - guess)

        # Hint System
        if difference > 20:
            print("🧊 Ice Cold!")
        elif difference > 10:
            print("🥶 Cold!")
        elif difference > 5:
            print("🌡️ Warm!")
        else:
            print("🔥 Hot!")

        # Hearts using FOR LOOP
        lives_left = max_attempts - attempts

        print("Remaining Lives: ", end="")
        for i in range(lives_left):
            print("❤️", end=" ")
        print()

# Win/Loss Message
if not won:
    print("\n💀 Game Over!")
    print("🔐 The secret number was:", secret)
else:
    print("🏆 You Win!")