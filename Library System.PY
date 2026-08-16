# 📚 Defence Mission Library

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print("❌ Sorry! This book is already borrowed.")
        else:
            self.is_borrowed = True
            print("✅ Book borrowed successfully:", self.title)

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print("🔄 Book returned successfully:", self.title)
        else:
            print("⚠️ This book was not borrowed.")


# Creating 3 Book objects
book1 = Book("Python for Young Coders", "Riya Sharma")
book2 = Book("Mission Defence", "Aman Verma")
book3 = Book("Journey to Space", "Neha Singh")


print("===================================")
print("📚 DEFENCE MISSION LIBRARY 📚")
print("===================================")

# Displaying book details
print("\n📖 Available Books:")
print("1.", book1.title, "-", book1.author)
print("2.", book2.title, "-", book2.author)
print("3.", book3.title, "-", book3.author)


# Borrowing books
print("\n🎯 BORROWING BOOKS")

book1.borrow()
book2.borrow()

# Trying to borrow the same book again
book1.borrow()


# Returning books
print("\n🔄 RETURNING BOOKS")

book1.return_book()
book2.return_book()


# Demonstrating the third book
print("\n🚀 THIRD BOOK DEMONSTRATION")

book3.borrow()
book3.return_book()


print("\n===================================")
print("🎉 Thank you for using the library!")
print("===================================")