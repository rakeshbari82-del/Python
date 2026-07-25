print("📚==============================================📚")
print("      🌟 SMART LIBRARY BOOK CHECKER 🌟")
print("📚==============================================📚")

# -----------------------------
# Book Names
# -----------------------------

books = [
    "Python",
    "Java",
    "C++",
    "HTML",
    "JavaScript",
    "AI Basics",
    "Cyber Security",
    "Data Science",
    "Machine Learning",
    "Cloud Computing"
]

# Copies Available
copies = [5, 0, 8, 2, 0, 7, 3, 4, 1, 6]

# Late Fee of Each Book
late_fee = [10, 15, 20, 10, 25, 30, 15, 20, 25, 30]

# ----------------------------------
# ZIP()
# ----------------------------------

library = dict(zip(books, copies))

print("\n📖 Books in Library:")
for book, copy in library.items():
    print(f"📚 {book:<20} ➜ {copy} Copies")

# ----------------------------------
# LIST COMPREHENSION
# ----------------------------------

available_books = [book for book in books if library[book] > 0]

print("\n✅ Available Books")
for book in available_books:
    print("📗", book)

# ----------------------------------
# FILTER()
# ----------------------------------

available = list(filter(lambda x: x > 0, copies))

print("\n📦 Available Copy Numbers")
print(available)

# ----------------------------------
# MAP()
# Increase Late Fee by 20%
# ----------------------------------

updated_fee = list(map(lambda x: int(x * 1.20), late_fee))

print("\n💰 Updated Late Fees")
for b, fee in zip(books, updated_fee):
    print(f"📘 {b:<20} 💲 {fee}")

# ----------------------------------
# DICTIONARY COMPREHENSION
# ----------------------------------

book_status = {
    book: ("✅ Available" if copy > 0 else "❌ Unavailable")
    for book, copy in zip(books, copies)
}

print("\n📋 Book Status")
for book, status in book_status.items():
    print(f"{book:<20} {status}")

# ----------------------------------
# Search Book
# ----------------------------------

while True:

    print("\n🔍 Search Any Book")
    name = input("👉 Enter Book Name : ")

    if name in library:

        if library[name] > 0:
            print("🎉 Book Available!")
            print(f"📚 Copies Left : {library[name]}")

        else:
            print("😔 Sorry! Book Not Available")

    else:
        print("❌ Book Not Found")

    ch = input("\nContinue Searching? (yes/no): ").lower()

    if ch == "no":
        break

# ----------------------------------
# Borrow Book
# ----------------------------------

print("\n📚 Borrow a Book")

while True:

    borrow = input("Enter Book Name : ")

    if borrow not in library:
        print("❌ Book Not Found")
        continue

    if library[borrow] == 0:
        print("🚫 This Book is Out of Stock")
        break

    library[borrow] -= 1

    print("🎉 Book Issued Successfully!")
    print(f"📖 Remaining Copies : {library[borrow]}")

    if library[borrow] == 0:
        print("⚠️ Book Just Became Unavailable!")
        break

    again = input("Borrow Another Book? (yes/no): ").lower()

    if again == "no":
        break

# ----------------------------------
# Final Report
# ----------------------------------

print("\n📊 FINAL LIBRARY REPORT")

for book, copy in library.items():

    if copy > 0:
        print(f"📗 {book:<20} {copy} Copies")
    else:
        print(f"📕 {book:<20} Out of Stock")

print("\n🏆 Most Available Book")

highest = max(library.values())

for book, copy in library.items():
    if copy == highest:
        print(f"🥇 {book} ({copy} Copies)")


print("\n🎯 Thank You For Using Smart Library!")
print("📚 Have a Nice Day 😊")