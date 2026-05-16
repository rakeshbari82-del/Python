# ==================================
#      SUMMER TIMES PROJECT
# ==================================

print("☀️ Welcome to Weather Fashion Advisor ☀️")

name = input("Enter your name: ")
temp = int(input("Enter temperature in °C: "))

print("\nChoose Weather")
print("1. Sunny")
print("2. Rainy")
print("3. Cold")

weather = input("Enter choice (1-3): ")

print("\n----------------------------")
print("Hello", name)
print("----------------------------")

# Conditional Statements

if weather == "1":

    print("🌞 Sunny Weather")

    if temp >= 30:
        print("👕 Wear cotton clothes")
        print("🧢 Use sunglasses or cap")
        print("🥤 Drink cold water")

    else:
        print("😊 Weather is pleasant")
        print("👚 Wear light clothes")

elif weather == "2":

    print("🌧️ Rainy Weather")

    if temp >= 20:
        print("☂️ Take an umbrella")
        print("👟 Wear waterproof shoes")

    else:
        print("🧥 Wear a raincoat")
        print("☕ Enjoy hot soup")

elif weather == "3":

    print("❄️ Cold Weather")

    if temp <= 10:
        print("🧣 Wear heavy jacket")
        print("🧤 Use gloves")

    else:
        print("🧥 Wear a sweater")

else:
    print("❌ Wrong choice entered")

print("\n✅ Stay safe and enjoy the weather!")