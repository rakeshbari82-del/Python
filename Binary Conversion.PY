# ==========================================
#      DIGITAL NUMBER LAB 🚀
# ==========================================

print("=" * 50)
print("🧪 WELCOME TO DIGITAL NUMBER LAB 🧪")
print("=" * 50)

name = input("👤 Enter Scientist Name: ")

total_conversions = 0

while True:

    print("\n" + "=" * 50)
    print("📋 MAIN MENU")
    print("=" * 50)

    print("1️⃣  Convert Decimal to Binary")
    print("2️⃣  View Scientist Status")
    print("3️⃣  Exit Lab")

    choice = input("\n👉 Enter your choice: ")

    # OPTION 1
    if choice == "1":

        while True:

            num = int(input("\n🔢 Enter a Decimal Number: "))

            original = num
            binary = ""

            if num == 0:
                binary = "0"

            else:
                while num > 0:
                    rem = num % 2
                    binary = str(rem) + binary
                    num = num // 2

            print("\n🚀 CONVERSION REPORT")
            print("-" * 40)
            print("Decimal Number :", original)
            print("Binary Number  :", binary)

            ones = binary.count("1")
            zeros = binary.count("0")

            print("\n📊 BINARY ANALYSIS")
            print("-" * 40)
            print("Total Digits :", len(binary))
            print("Number of 1s :", ones)
            print("Number of 0s :", zeros)

            # Fun Analysis
            if ones > zeros:
                print("⚡ Power Level : HIGH")
            elif zeros > ones:
                print("🛰️ Power Level : STABLE")
            else:
                print("🌟 Power Level : BALANCED")

            # Special Numbers
            if original % 2 == 0:
                print("✅ EVEN NUMBER DETECTED")
            else:
                print("🔥 ODD NUMBER DETECTED")

            if original > 100:
                print("🏆 BONUS: Large Number Explorer!")
            else:
                print("🎯 BONUS: Beginner Explorer!")

            total_conversions += 1

            again = input("\n🔄 Convert another number? (Yes/No): ")

            if again.lower() != "yes":
                break

    # OPTION 2
    elif choice == "2":

        print("\n👨‍🔬 SCIENTIST REPORT")
        print("-" * 40)
        print("Scientist Name :", name)
        print("Conversions Done :", total_conversions)

        if total_conversions >= 10:
            print("🏅 MASTER BINARY SCIENTIST")
        elif total_conversions >= 5:
            print("🥈 ADVANCED SCIENTIST")
        elif total_conversions >= 1:
            print("🥉 BEGINNER SCIENTIST")
        else:
            print("📚 TRAINING MODE")

    # OPTION 3
    elif choice == "3":

        print("\n🚪 Exiting Digital Number Lab...")
        print("👋 Thank You,", name)
        print("🌟 Keep Exploring Programming!")
        break

    else:
        print("❌ Invalid Choice! Try Again.")