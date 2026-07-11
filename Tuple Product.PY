import time

print("=" * 50)
print("🎮 WELCOME TO TUPLE PRODUCT CHALLENGE 🎮")
print("=" * 50)

time.sleep(1)

# Input
n = int(input("\n🔢 How many numbers do you want in your tuple? : "))

numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

my_tuple = tuple(numbers)

print("\n✨ Your Tuple is:", my_tuple)

# Product
product = 1
for i in my_tuple:
    product *= i

# Sum
total = sum(my_tuple)

# Display Results
print("\n📊 RESULT")
print("-" * 30)
print("➕ Sum =", total)
print("✖️ Product =", product)
print("🔺 Largest =", max(my_tuple))
print("🔻 Smallest =", min(my_tuple))
print("🔢 Total Elements =", len(my_tuple))

# Guessing Game
print("\n🎯 MINI GAME")
guess = int(input("Guess the Product of the tuple: "))

if guess == product:
    print("🎉 Amazing! Correct Answer!")
    stars = 5
else:
    print("❌ Oops! Wrong Guess.")
    print("✅ Correct Product is:", product)

    difference = abs(product - guess)

    if difference <= 10:
        stars = 4
    elif difference <= 30:
        stars = 3
    elif difference <= 60:
        stars = 2
    else:
        stars = 1

print("\n⭐ Your Rating:", "⭐" * stars)

print("\n💡 Fun Facts")
print("Tuple is Immutable ✅")
print("It cannot be changed after creation.")
print("Product is obtained by multiplying all elements.")

print("\n🎊 Thank You for Playing! 🎊")