# ==========================================================
#      🚀 ULTIMATE NUMBER DETECTIVE AGENCY 🚀
# ==========================================================

print("==========================================================")
print("     🚀 ULTIMATE NUMBER DETECTIVE AGENCY 🚀              ")
print("==========================================================\n")

print("🌟 Welcome to the ULTIMATE NUMBER DETECTIVE 🌟")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
print("🤖 This smart AI machine will investigate your number!")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# User Input
num = int(input("🎯 Enter your secret number: "))

# Store original number
original = num

# Variables
count = 0
reverse = 0
sum_digits = 0
largest = 0
smallest = 9

# Armstrong Variables
temp = original
digits = len(str(original))
armstrong_sum = 0

# Special case for 0
if num == 0:
    count = 1
    reverse = 0
    largest = 0
    smallest = 0

# ==========================================================
#                MAIN WHILE LOOP
# ==========================================================

while num > 0:

    digit = num % 10

    # Count digits
    count += 1

    # Reverse Number
    reverse = reverse * 10 + digit

    # Sum of digits
    sum_digits += digit

    # Largest digit
    if digit > largest:
        largest = digit

    # Smallest digit
    if digit < smallest:
        smallest = digit

    # Remove last digit
    num = num // 10

# ==========================================================
#             ARMSTRONG NUMBER CHECK
# ==========================================================

while temp > 0:

    digit = temp % 10

    armstrong_sum = armstrong_sum + (digit ** digits)

    temp = temp // 10

# ==========================================================
#                    FINAL REPORT
# ==========================================================

print("\n📂 SCANNING COMPLETE...")
print("═══════════════════════════════════")

print(f"🔢 Original Number      : {original}")
print(f"📏 Total Digits         : {count}")
print(f"🔄 Reverse Number       : {reverse}")
print(f"➕ Sum of Digits        : {sum_digits}")
print(f"🏆 Largest Digit        : {largest}")
print(f"🎯 Smallest Digit       : {smallest}")

print("═══════════════════════════════════")

# Even or Odd
if original % 2 == 0:
    print("⚡ STATUS : EVEN NUMBER")
else:
    print("🔥 STATUS : ODD NUMBER")

# Palindrome Check
if original == reverse:
    print("🪞 RESULT : PALINDROME NUMBER")
else:
    print("❌ RESULT : NOT A PALINDROME")

# Armstrong Check
if original == armstrong_sum:
    print("💎 WOW! It is an ARMSTRONG NUMBER")
else:
    print("🚫 It is NOT an Armstrong Number")

# Spy Rank System
print("\n🕵️ AGENT RANK ANALYSIS 🕵️")

if count >= 10:
    print("👑 Rank : LEGENDARY NUMBER MASTER")
elif count >= 7:
    print("🚀 Rank : ELITE NUMBER AGENT")
elif count >= 5:
    print("😎 Rank : SENIOR DETECTIVE")
else:
    print("🎓 Rank : BEGINNER SPY")

# Bonus Secret Checks
print("\n🎲 BONUS SECRET CHECKS 🎲")

if sum_digits % 3 == 0:
    print("✨ Number is divisible by 3")
else:
    print("🌙 Number is NOT divisible by 3")

if original % 5 == 0:
    print("💰 Jackpot! Number ends with 0 or 5")
else:
    print("🔒 Secure Number Activated")

# AI Funny Messages
print("\n🤖 AI SYSTEM MESSAGE 🤖")

if largest == 9:
    print("🚨 ALERT! Maximum Power Digit Found!")
else:
    print("✅ Stable Number Energy Found!")

if original > 100000:
    print("🌌 Cosmic Level Number Detected!")
elif original > 1000:
    print("🚀 Powerful Number Detected!")
else:
    print("😊 Cute Small Number Found!")

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("🎉 Mission Completed Successfully 🎉")
print("💖 Thanks for using ULTIMATE NUMBER DETECTIVE 💖")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")