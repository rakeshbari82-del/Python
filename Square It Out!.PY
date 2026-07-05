import random
import time

print("🌟" + "="*65 + "🌟")
print("            🎲 SQUARE IT OUT! 🎲")
print("      💻 Python Lists Fun Project 💻")
print("🌟" + "="*65 + "🌟")

time.sleep(1)

# User Input
start = int(input("\n🔢 Enter Starting Number : "))
end = int(input("🔢 Enter Ending Number   : "))

if start > end:
    start, end = end, start

# Number List
numbers = list(range(start, end + 1))

# Square List
squares = [i**2 for i in numbers]

print("\n📋 Numbers List")
print(numbers)

print("\n🟦 Square List")
print(squares)

# Even Squares
even = []
odd = []

for i in squares:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("\n💙 Even Square Numbers")
print(even)

print("\n❤️ Odd Square Numbers")
print(odd)

# Statistics
print("\n📊 Project Statistics")
print("🔸 Total Numbers :", len(numbers))
print("🔸 Biggest Square :", max(squares))
print("🔸 Smallest Square:", min(squares))
print("🔸 Sum of Squares :", sum(squares))
print("🔸 Average :", round(sum(squares)/len(squares),2))

# Search Number
print("\n🔍 Search Square")
num = int(input("Enter a number : "))

if num in numbers:
    print("✅ Square of", num, "=", num**2)
else:
    print("❌ Number not found in the list.")

# ---------------- GAME ----------------

print("\n🎮 MINI GAME : Guess the Square!")
time.sleep(1)

secret = random.choice(numbers)

print("👉 Guess the square of", secret)

guess = int(input("Your Answer : "))

if guess == secret**2:
    print("🎉🎉 Correct!! You Win!")
else:
    print("😅 Wrong!")
    print("✅ Correct Answer :", secret**2)

# Bonus Table
print("\n📚 Square Table")
print("-"*30)

for n, s in zip(numbers, squares):
    print(f"{n:3}  ➜  {s}")

print("-"*30)

print("\n🏆 Thanks for Playing!")
print("⭐ Keep Learning Python ⭐")