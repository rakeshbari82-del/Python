import random
import time

months = [
    ("January",31,"❄ Winter"),
    ("February",28,"❄ Winter"),
    ("March",31,"🌸 Spring"),
    ("April",30,"🌸 Spring"),
    ("May",31,"☀ Summer"),
    ("June",30,"☀ Summer"),
    ("July",31,"🌧 Rainy"),
    ("August",31,"🌧 Rainy"),
    ("September",30,"🍂 Autumn"),
    ("October",31,"🍂 Autumn"),
    ("November",30,"❄ Winter"),
    ("December",31,"❄ Winter")
]

facts = {
"January":"🎆 New Year begins!",
"February":"❤️ Chocolate's Month.",
"March":"🌸 Flowers bloom.",
"April":"😂 April Fool's Month.",
"May":"🌞 Summer Vacation begins.",
"June":"🏖 Perfect for holidays.",
"July":"🌧 Monsoon starts.",
"August":"🇮🇳 Independence Day (India).",
"September":"📚 Schools are busy.",
"October":"🎃 Halloween Month.",
"November":"🪔 Festival Season.",
"December":"🎄 Christmas & New Year."
}

print("\n")
print("🌈"*20)
print("🎉✨ WELCOME TO THE SMART MONTH EXPLORER ✨🎉")
print("🌈"*20)

print("\nLoading", end="")

for i in range(10):
    print("⏳", end="", flush=True)
    time.sleep(0.2)

print("\n✅ Program Loaded Successfully!\n")

while True:

    print("\n"+"═"*55)
    print("📅 MAIN MENU")
    print("═"*55)

    print("1️⃣  📜 Show All Months")
    print("2️⃣  🔍 Search a Month")
    print("3️⃣  🎲 Lucky Month")
    print("4️⃣  💡 Random Month Fact")
    print("5️⃣  📊 Month Statistics")
    print("6️⃣  ❌ Exit")

    choice = input("\n👉 Enter your choice : ")

    if choice=="1":

        print("\n🏆 LIST OF ALL MONTHS 🏆\n")

        for i,m in enumerate(months,start=1):
            print(f"{i:2}. 📅 {m[0]:12} | {m[1]} Days | {m[2]}")

    elif choice=="2":

        name=input("\n🔍 Enter Month Name : ").title()

        found=False

        for i,m in enumerate(months,start=1):

            if m[0]==name:
                print("\n"+"⭐"*25)
                print("📖 MONTH DETAILS")
                print("⭐"*25)
                print("📅 Month :",m[0])
                print("🔢 Number :",i)
                print("🗓 Days :",m[1])
                print("🌍 Season :",m[2])
                print("💡 Fact :",facts[m[0]])
                found=True
                break

        if not found:
            print("❌ Month Not Found!")

    elif choice=="3":

        lucky=random.choice(months)

        print("\n🎲 YOUR LUCKY MONTH IS...")
        time.sleep(1)

        print("✨"*20)
        print("🎉",lucky[0],"🎉")
        print("🗓 Days :",lucky[1])
        print("🌍 Season :",lucky[2])
        print("💡",facts[lucky[0]])
        print("✨"*20)

    elif choice=="4":

        month=random.choice(list(facts.keys()))

        print("\n🎁 RANDOM MONTH FACT")
        print("📅",month)
        print(facts[month])

    elif choice=="5":

        print("\n📊 MONTH STATISTICS")
        print("📅 Total Months : 12")
        print("🗓 Total Days (Normal Year) : 365")
        print("❄ Winter Months : 4")
        print("🌸 Spring Months : 2")
        print("☀ Summer Months : 2")
        print("🌧 Rainy Months : 2")
        print("🍂 Autumn Months : 2")

    elif choice=="6":

        print("\n🌸 Thank You For Using Smart Month Explorer 🌸")
        print("😊 Keep Learning Python! 🚀")
        break

    else:
        print("❌ Invalid Choice! Try Again.")