# ╔══════════════════════════════════════════════════════╗
#          🎂✨ SUPER SMART AGE ADVISOR ✨🎂
# ╚══════════════════════════════════════════════════════╝

print("🌟━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🌟")
print("🤖        WELCOME TO AGE ADVISOR PRO         🤖")
print("🌟━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🌟")

# Taking age input from user
age = int(input("\n🪄 Enter your age: "))

print("\n🔍 Analyzing Your Age Data...")
print("⚡ Smart System Activated ⚡")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# Valid age check
if age > 0:

    # Nested condition for age between 10 and 20
    if age >= 10:

        if age <= 20:

            print(f"🟢 AWESOME! You are {age} years old 🎉")
            print("✅ Your age is BETWEEN 10 and 20.")
            print("🎯 You are in the best learning stage!")

            # Advice according to age
            if age >= 10 and age <= 13:
                print("\n📚 ADVICE FOR YOU:")
                print("🌈 Focus on studies and build good habits.")
                print("⚽ Play outdoor games and stay active.")
                print("📖 Read fun and educational books.")

            elif age >= 14 and age <= 16:
                print("\n📚 ADVICE FOR YOU:")
                print("💻 Start learning coding and new skills.")
                print("🎯 Stay focused on your goals.")
                print("🧠 Believe in yourself and avoid distractions.")

            else:
                print("\n📚 ADVICE FOR YOU:")
                print("🚀 Work hard for your dreams and career.")
                print("📘 Improve communication and leadership skills.")
                print("🌟 Success comes with consistency!")

        else:
            print(f"🔵 You are {age} years old.")
            print("❌ Your age is ABOVE 20.")

            print("\n💡 LIFE ADVICE:")
            print("💼 Focus on career growth and self-improvement.")
            print("🏋️ Stay healthy and manage your time wisely.")
            print("🌍 Keep learning new things every day.")

    else:
        print(f"🟡 You are {age} years old.")
        print("❌ Your age is BELOW 10.")

        print("\n🎈 LITTLE STAR ADVICE:")
        print("🧸 Enjoy your childhood and have fun.")
        print("📚 Learn new things with curiosity.")
        print("🍎 Eat healthy food and listen to parents.")

# Invalid age
else:
    print("🚫 INVALID AGE ENTERED!")
    print("⚠️ Age cannot be zero or negative.")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("💖 Thank You for Using Smart Age Advisor 💖")
print("🌟 Keep Smiling • Keep Learning • Keep Growing 🌟")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")