import random
import string

print("🔐===========================================🔐")
print("      🎉 RANDOM PASSWORD GENERATOR 🎉")
print("🔐===========================================🔐")

print("\nChoose Password Strength")
print("1️⃣ Weak")
print("2️⃣ Medium")
print("3️⃣ Strong")

choice = input("\n👉 Enter your choice (1/2/3): ")

if choice == "1":
    length = 6
elif choice == "2":
    length = 10
elif choice == "3":
    length = 14
else:
    print("⚠️ Invalid Choice! Using Medium Password.")
    length = 10

# Characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = "!@#$%^&*?"

# Combine all characters
all_characters = lower + upper + numbers + symbols

# Generate password
password = ""

for i in range(length):
    password += random.choice(all_characters)

# Shuffle password
password = list(password)
random.shuffle(password)
password = "".join(password)

print("\n✨ Your Password is ✨")
print("🔑", password)

# Password Strength

print("\n📊 Password Strength")

if length == 6:
    print("🔴 Weak Password")
elif length == 10:
    print("🟡 Medium Password")
else:
    print("🟢 Strong Password")

print("\n🎊 Stay Safe! Never share your password.")
print("😊 Thank You for using the Password Generator!")