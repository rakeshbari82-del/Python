# ===================================================
#         ⚡ SUPER POWER CALCULATOR ⚡
# ===================================================

print("===================================================")
print("        ⚡ SUPER POWER CALCULATOR ⚡              ")
print("===================================================\n")

print("🌟 Welcome to the Super Power Calculator 🌟")
print("This program finds the power of any number using loops!\n")

# Taking user input
name = input("👤 Enter your name: ")

base = int(input("\n🔢 Enter the base number: "))
power = int(input("💥 Enter the power value: "))

# Starting value
result = 1

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"🧠 Hello {name}, your calculation is starting...")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

# Loop for power calculation
for i in range(1, power + 1):
    result = result * base
    
    print(f"⚡ Step {i}")
    print(f"👉 {base} × itself {i} time(s)")
    print(f"✅ Current Result = {result}")
    print("-----------------------------")

# Final Answer
print("\n🎯 FINAL RESULT 🎯")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"📌 {base}^{power} = {result}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# Special Messages
if result >= 100000:
    print("🚀 Incredible! That's a SUPER HUGE number!")
elif result >= 1000:
    print("🔥 Amazing! That's a very big value!")
elif result >= 100:
    print("😎 Cool! Nice powerful calculation!")
else:
    print("😊 Good job! Simple and clean calculation!")


# Even or Odd Check
if result % 2 == 0:
    print("🔵 The final result is EVEN.")
else:
    print("🟣 The final result is ODD.")
    

# Bonus Fun Facts
print("\n🎁 BONUS INFORMATION 🎁")
print(f"🔹 Square of {base} = {base * base}")
print(f"🔹 Cube of {base} = {base * base * base}")

# Thank You Message
print("\n💖 Thank you for using Super Power Calculator 💖")
print("🌈 Keep Learning Python & Keep Growing 🌈")