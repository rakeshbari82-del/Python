# ============================================
# 🎓🌟 SMART STUDENT GRADE BOOK 🌟🎓
# ============================================

print("📚========================================📚")
print("      🎓 SMART STUDENT GRADE BOOK 🎓")
print("📚========================================📚")

# Dictionary
students = {
    "Aarav": 92,
    "Kabir": 87,
    "Riya": 95,
    "Rahul": 76,
    "Priya": 89,
    "Aarul": 98,
    "Neha": 81
}

print("\n👨‍🎓 Student Marks")
print("-" * 35)

# Display Students
for name, marks in students.items():
    print(f"🧑 {name:<10} ➜ {marks} Marks")

# -------------------------
# Calculate Average
# -------------------------
total = 0

for marks in students.values():
    total += marks

average = total / len(students)

print("\n📊 Class Report")
print("-" * 35)
print(f"📚 Total Students : {len(students)}")
print(f"📈 Class Average : {average:.2f}")

# -------------------------
# Highest Score
# -------------------------
highest = max(students.values())

for name, marks in students.items():
    if marks == highest:
        topper = name

print(f"\n🏆 Topper : {topper}")
print(f"🥇 Highest Marks : {highest}")

# -------------------------
# Lowest Score
# -------------------------
lowest = min(students.values())

for name, marks in students.items():
    if marks == lowest:
        low_student = name

print(f"\n😅 Lowest Scorer : {low_student}")
print(f"📉 Lowest Marks : {lowest}")

# -------------------------
# Grade Section
# -------------------------
print("\n🎖️ Student Grades")
print("-" * 35)

for name, marks in students.items():

    if marks >= 90:
        grade = "A+ 🌟"

    elif marks >= 80:
        grade = "A 😊"

    elif marks >= 70:
        grade = "B 👍"

    elif marks >= 60:
        grade = "C 🙂"

    else:
        grade = "D 😢"

    print(f"{name:<10} ➜ {marks} ➜ {grade}")

# -------------------------
# Search Student
# -------------------------
print("\n🔍 Student Search")
print("-" * 35)

search = input("👤 Enter Student Name : ")

score = students.get(search)

if score is None:
    print("❌ Student Not Found!")

else:
    print(f"\n🎉 Student Found!")
    print(f"👨‍🎓 Name : {search}")
    print(f"📚 Marks : {score}")

    if score >= 90:
        print("🏅 Grade : A+ 🌟")

    elif score >= 80:
        print("🎖️ Grade : A 😊")

    elif score >= 70:
        print("👍 Grade : B")

    elif score >= 60:
        print("🙂 Grade : C")

    else:
        print("😢 Grade : D")

print("\n🎉========================================🎉")
print("     ✅ THANK YOU FOR USING GRADE BOOK")
print("🎉========================================🎉")