print("=" * 50)
print("       Avika's Pattern Experiment Lab")
print("=" * 50)

rows = int(input("Enter the number of rows: "))

print("\n1. Star Triangle ⭐")
print("2. Number Triangle 🔢")
print("3. Alphabet Triangle 🔤")
print("4. Diamond Shape 💎")
print("5. Emoji Triangle 😀")

choice = int(input("\nChoose Pattern (1-5): "))

print("\nGenerated Pattern:\n")

# Star Triangle
if choice == 1:
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

# Number Triangle
elif choice == 2:
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Alphabet Triangle
elif choice == 3:
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        ch = 65
        for j in range(i):
            print(chr(ch), end=" ")
            ch += 1
        print()

# Diamond Shape
elif choice == 4:
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * i)

    print("\n💎 Diamond Shape Created!")

# Emoji Triangle
elif choice == 5:

    print("\nChoose an Emoji:")
    print("1. 🥧 Pie")
    print("2. 🍕 Pizza")
    print("3. 🌸 Flower")
    print("4. ⭐ Star")
    print("5. 🦋 Butterfly")
    print("6. ❤️ Heart")
    print("7. 😎 Smiley")

    emoji_choice = input("\nEnter emoji choice (1-7): ")

    emoji_dict = {
        "1": "🥧",
        "2": "🍕",
        "3": "🌸",
        "4": "⭐",
        "5": "🦋",
        "6": "❤️",
        "7": "😎"
    }

    emoji = emoji_dict.get(emoji_choice, "⭐")

    for i in range(1, rows + 1):
        print(" " * (rows - i) + (emoji + " ") * i)

    print("\n🌈 Emoji Pattern Created!")

else:
    print("❌ Invalid Choice!")

print("\n🎉 Pattern Created Successfully!")
print("=" * 50)