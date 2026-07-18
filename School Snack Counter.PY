import array as arr

print("🏫======================================================🏫")
print("          🍔 SMART SCHOOL SNACK COUNTER 🍕")
print("🏫======================================================🏫")


# Weekly Snack Menus

monday = {
    "Burger",
    "Pizza",
    "Sandwich",
    "Juice"
}

tuesday = {
    "Pizza",
    "Fries",
    "Juice",
    "Cake",
    "Momos"
}

wednesday = {
    "Pasta",
    "Sandwich",
    "Milk",
    "Apple",
    "Pizza"
}

thursday = {
    "Noodles",
    "Burger",
    "Juice",
    "Ice Cream",
    "Fries"
}

friday = {
    "Pav Bhaji",
    "Pizza",
    "Sandwich",
    "Cold Drink",
    "Cake"
}

saturday = {
    "Dosa",
    "Idli",
    "Burger",
    "Milk Shake",
    "Juice"
}

print("\n📅 Monday Menu")
print(monday)

print("\n📅 Tuesday Menu")
print(tuesday)

print("\n📅 Wednesday Menu")
print(wednesday)

print("\n📅 Thursday Menu")
print(thursday)

print("\n📅 Friday Menu")
print(friday)

print("\n📅 Saturday Menu")
print(saturday)

print("\n🆕 Today's Special Snacks Added!")

monday.add("Ice Cream")
tuesday.add("Pasta")
wednesday.add("French Fries")
thursday.add("Samosa")
friday.add("Chocolate")
saturday.add("Popcorn")

print("\n🍔 Monday :", monday)
print("🍕 Tuesday :", tuesday)
print("🥪 Wednesday :", wednesday)
print("🍜 Thursday :", thursday)
print("🍰 Friday :", friday)
print("🥤 Saturday :", saturday)

# Common Snacks
common_mt = monday.intersection(tuesday)
common_wt = wednesday.intersection(thursday)
common_fs = friday.intersection(saturday)

print("\n🤝 Common Snacks")

print("Monday & Tuesday :", common_mt)
print("Wednesday & Thursday :", common_wt)
print("Friday & Saturday :", common_fs)

# Sales Array
sales = arr.array('i', [45, 30, 60, 20, 55, 40])

print("\n📊 Weekly Snack Sales")
print(sales)

sales.insert(0, 15)
sales.append(70)

print("\n📈 Updated Weekly Sales")
print(sales)

print("\n🔍 Sales Count")

print("20 Sold =", sales.count(20), "time(s)")
print("30 Sold =", sales.count(30), "time(s)")
print("40 Sold =", sales.count(40), "time(s)")
print("70 Sold =", sales.count(70), "time(s)")

sales.reverse()

print("\n🔄 Reverse Weekly Sales")
print(sales)

print("\n🏆================= FINAL WEEKLY REPORT =================🏆")

print("🍔 Monday Menu :", monday)
print("🍕 Tuesday Menu :", tuesday)
print("🥪 Wednesday Menu :", wednesday)
print("🍜 Thursday Menu :", thursday)
print("🍰 Friday Menu :", friday)
print("🥤 Saturday Menu :", saturday)

print("\n🤝 Common Snacks")
print("Monday & Tuesday :", common_mt)
print("Wednesday & Thursday :", common_wt)
print("Friday & Saturday :", common_fs)

print("\n📊 Final Sales :", sales)

print("\n⭐ Total Monday Snacks :", len(monday))
print("⭐ Total Tuesday Snacks :", len(tuesday))
print("⭐ Total Wednesday Snacks :", len(wednesday))
print("⭐ Total Thursday Snacks :", len(thursday))
print("⭐ Total Friday Snacks :", len(friday))
print("⭐ Total Saturday Snacks :", len(saturday))

print("\n🎉 Thank You for Visiting Our School Canteen!")
print("🍔🍟🥪🍕🥤 Have a Nice Day! 😊")