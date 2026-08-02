# ==========================================
# 🌞 DAILY DATA HELPER 📅
# 👨‍💻 Object-Oriented Programming Project
# ==========================================

class DailyDataHelper:

    app_name = "🌞 Daily Data Helper"

    # Constructor
    def __init__(self, name):
        self.name = name
        self.tasks = []

        print("=" * 45)
        print(f"🎉 Welcome {self.name}!")
        print(f"📱 {DailyDataHelper.app_name} Started")
        print("=" * 45)

    # Add Task
    def add_task(self):
        task = input("📝 Enter today's task: ")
        self.tasks.append(task)
        print("✅ Task Added Successfully!\n")

    # Show Tasks using enumerate()
    def show_tasks(self):

        print("\n📋 Today's Task List")
        print("-" * 30)

        if len(self.tasks) == 0:
            print("😴 No Tasks Available")
        else:
            for index, value in enumerate(self.tasks, start=1):
                print(f"{index}. {value} ✅")

    # Search Task
    def search_task(self):

        word = input("\n🔍 Enter task to search: ")

        found = False

        for index, value in enumerate(self.tasks, start=1):

            if word.lower() == value.lower():
                print(f"🎯 Found at Task No. {index}")
                found = True

        if not found:
            print("❌ Task Not Found")

    # Delete Task
    def delete_task(self):

        self.show_tasks()

        if len(self.tasks) == 0:
            return

        num = int(input("\n🗑 Enter Task Number to Delete: "))

        if 1 <= num <= len(self.tasks):

            removed = self.tasks.pop(num-1)

            print(f"🗑 '{removed}' Deleted Successfully!")

        else:
            print("❌ Invalid Number")

    # Statistics
    def statistics(self):

        print("\n📊 DAILY REPORT")
        print("-" * 25)

        print(f"👤 User : {self.name}")
        print(f"📌 Total Tasks : {len(self.tasks)}")

        if len(self.tasks) >= 5:
            print("🏆 Excellent Productivity!")
        elif len(self.tasks) >= 3:
            print("😊 Good Job!")
        elif len(self.tasks) >= 1:
            print("👍 Keep Going!")
        else:
            print("😴 Add Some Tasks!")

    # Destructor
    def __del__(self):
        print("\n👋 Closing Daily Data Helper...")
        print("💖 Have a Wonderful Day!")
        print("🌟 Goodbye!\n")


# ==========================
# Main Program
# ==========================

name = input("👤 Enter Your Name: ")

obj = DailyDataHelper(name)

while True:

    print("\n==============================")
    print("🌞 DAILY DATA HELPER MENU")
    print("==============================")

    print("1️⃣ Add Task")
    print("2️⃣ Show Tasks")
    print("3️⃣ Search Task")
    print("4️⃣ Delete Task")
    print("5️⃣ Daily Report")
    print("6️⃣ Exit")

    choice = input("\n👉 Enter Choice: ")

    if choice == "1":
        obj.add_task()

    elif choice == "2":
        obj.show_tasks()

    elif choice == "3":
        obj.search_task()

    elif choice == "4":
        obj.delete_task()

    elif choice == "5":
        obj.statistics()

    elif choice == "6":
        print("\n🙏 Thanks for using the program!")
        del obj
        break

    else:
        print("❌ Invalid Choice")