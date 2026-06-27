import time

print("╔════════════════════════════════════════════╗")
print("║      🎯 AGE MASTER - EXCEPTION GAME 🎯     ║")
print("╚════════════════════════════════════════════╝")

print("\nLoading Project", end="")
for i in range(5):
    print(".", end="", flush=True)
    time.sleep(0.4)

while True:

    print("\n\n📋 MAIN MENU")
    print("1️⃣  Check Age Validation")
    print("2️⃣  Divide Two Numbers")
    print("3️⃣  Check Even or Odd")
    print("4️⃣  Exit")

    choice = input("\n👉 Enter Your Choice (1-4): ")

    # ===========================
    # AGE VALIDATION
    # ===========================
    if choice == "1":

        try:
            age = int(input("\n🎂 Enter Your Age : "))

            if age < 18:
                raise ValueError

            print("✅ Congratulations! Age is Valid.")

            if age % 2 == 0:
                print("🔵 Your age is EVEN.")
            else:
                print("🟢 Your age is ODD.")

        except ValueError:
            print("❌ Invalid Age! Age must be 18 or above.")

    # ===========================
    # DIVISION
    # ===========================
    elif choice == "2":

        try:
            num1, num2 = eval(input("\nEnter Two Numbers (Example: 10,2): "))

            result = num1 / num2

            print("✅ Result =", result)

        except ZeroDivisionError:
            print("❌ Cannot Divide by Zero.")

        except SyntaxError:
            print("❌ Please Separate Numbers with a Comma.")

        except:
            print("❌ Wrong Input.")

        else:
            print("🎉 Division Completed Successfully.")

        finally:
            print("📌 This block always executes.")

    # ===========================
    # EVEN OR ODD
    # ===========================
    elif choice == "3":

        valid = False

        while not valid:

            try:

                n = int(input("\nEnter a Number : "))

                if n % 2 == 0:
                    print("🔵 Number is EVEN")
                else:
                    print("🟢 Number is ODD")

                valid = True

            except ValueError:
                print("❌ Please Enter Numbers Only.")

    # ===========================
    # EXIT
    # ===========================
    elif choice == "4":

        print("\n🙏 Thank You for Using AGE MASTER.")
        print("👋 Have a Nice Day!")
        break

    else:
        print("❌ Invalid Choice! Please Select 1-4.")