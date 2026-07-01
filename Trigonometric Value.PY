# ===============================================
#      📐 TRIGONOMETRIC VALUE EXPLORER 📐
#         Random + Math Module Project
#             Made by: Your Name
# ===============================================

import math
import random
import time

# -------------------------------
# Welcome Screen
# -------------------------------

print("🌟" + "="*65 + "🌟")
print("        📚 WELCOME TO THE MATH EXPLORER 📚")
print("           🔢 Random & Math Module Project 🔢")
print("🌟" + "="*65 + "🌟")

time.sleep(1)

print("""
🎯 Goal:
This project helps you understand the Math Module
through interesting calculations and Trigonometry.
""")

quotes = [
    "✨ Mathematics is the language of the universe.",
    "🚀 Practice makes mathematics easy.",
    "💡 Every expert was once a beginner.",
    "🌈 Small steps every day create big success.",
    "🏆 Believe in yourself and solve confidently!"
]

print(random.choice(quotes))
print()

# -------------------------------
# MENU
# -------------------------------

while True:

    print("\n" + "="*55)
    print("📋 MAIN MENU")
    print("="*55)

    print("1️⃣  Floor & Ceiling")
    print("2️⃣  Copy Sign")
    print("3️⃣  Absolute Value")
    print("4️⃣  Greatest Common Divisor (GCD)")
    print("5️⃣  Square Root Finder")
    print("6️⃣  Trigonometric Values")
    print("7️⃣  Random Motivation")
    print("8️⃣  Exit")

    print("="*55)

    choice = input("👉 Enter your choice (1-8): ")

    # ----------------------------------
    # Floor & Ceiling
    # ----------------------------------

    if choice == "1":

        print("\n📌 FLOOR & CEILING")

        number = float(input("Enter a decimal number: "))

        print("⬆ Ceiling Value :", math.ceil(number))
        print("⬇ Floor Value   :", math.floor(number))

    # ----------------------------------
    # Copy Sign
    # ----------------------------------

    elif choice == "2":

        print("\n📌 COPY SIGN")

        x = float(input("Enter first number : "))
        y = float(input("Enter second number : "))

        print("Result :", math.copysign(x, y))

    # ----------------------------------
    # Absolute Value
    # ----------------------------------

    elif choice == "3":

        print("\n📌 ABSOLUTE VALUE")

        number = float(input("Enter any number : "))

        print("Absolute Value =", math.fabs(number))

    # ----------------------------------
    # GCD
    # ----------------------------------

    elif choice == "4":

        print("\n📌 GREATEST COMMON DIVISOR")

        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))

        print("GCD =", math.gcd(a, b))

    # ----------------------------------
    # Square Root Finder
    # ----------------------------------

    elif choice == "5":

        print("\n📌 SQUARE ROOT FINDER")

        number = float(input("Enter Square Number : "))

        if number < 0:
            print("❌ Square root of negative number is not possible.")
        else:
            answer = math.sqrt(number)
            print("✅ Square Root =", answer)

    # ----------------------------------
    # Trigonometric Values
    # ----------------------------------

    elif choice == "6":

        print("\n📐 TRIGONOMETRIC VALUES")

        degree = float(input("Enter Angle (Degree): "))

        radian = math.radians(degree)

        print("-"*45)

        print("sin(", degree, ") =", round(math.sin(radian),4))
        print("cos(", degree, ") =", round(math.cos(radian),4))

        if round(math.cos(radian),10)==0:
            print("tan(", degree, ") = Undefined")
        else:
            print("tan(", degree, ") =", round(math.tan(radian),4))

    # ----------------------------------
    # Random Quote
    # ----------------------------------

    elif choice == "7":

        print("\n🎉 Today's Motivation")
        print(random.choice(quotes))

    # ----------------------------------
    # Exit
    # ----------------------------------

    elif choice == "8":

        print("\n🙏 Thank You For Using")
        print("📚 Trigonometric Value Explorer")
        print("🌟 Keep Learning Mathematics 🌟")
        break

    else:
        print("❌ Invalid Choice! Please Enter 1-8.")