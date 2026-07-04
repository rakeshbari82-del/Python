import time

# ==============================
# 🌟 FUNCTION CALCULATOR PROJECT 🌟
# ==============================

print("🌈" + "=" * 60 + "🌈")
print("          🧮 WELCOME TO FUNCTION CALCULATOR 🧮")
print("         🚀 Python Project with Functions 🚀")
print("=" * 62)

time.sleep(1)

# ---------------- Functions ----------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

# ---------------- Main Program ----------------

while True:

    print("\n📋 Choose an Operation")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("1️⃣  Addition (+)")
    print("2️⃣  Subtraction (-)")
    print("3️⃣  Multiplication (×)")
    print("4️⃣  Division (÷)")
    print("5️⃣  Exit")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    choice = input("👉 Enter your choice (1-5): ")

    if choice == "5":
        print("\n🙏 Thank You for using the Calculator!")
        print("💙 Have a Wonderful Day!")
        break

    try:
        num1 = float(input("\n🔢 Enter First Number : "))
        num2 = float(input("🔢 Enter Second Number : "))

        if choice == "1":
            result = add(num1, num2)
            print(f"\n✅ {num1} + {num2} = {result}")

        elif choice == "2":
            result = subtract(num1, num2)
            print(f"\n✅ {num1} - {num2} = {result}")

        elif choice == "3":
            result = multiply(num1, num2)
            print(f"\n✅ {num1} × {num2} = {result}")

        elif choice == "4":
            result = divide(num1, num2)
            print(f"\n✅ {num1} ÷ {num2} = {result}")

        else:
            print("\n❌ Invalid Choice!")
            continue

    except ZeroDivisionError:
        print("\n🚫 Error!")
        print("You cannot divide a number by ZERO.")

    except ValueError:
        print("\n⚠ Invalid Input!")
        print("Please enter only numbers.")

    except Exception as e:
        print("\n❌ Unexpected Error:", e)

    print("\n" + "-" * 50)