# 🔐 Smart Account PIN Safety Checker
# Project based on Encapsulation and Special Functions

class Account:

    def __init__(self, name, pin):
        self.name = name
        self.__pin = pin          # 🔒 Private variable
        self.__status = "Not Checked"

    # 🔍 Private method to check PIN safety
    def __check_pin(self):

        if len(str(self.__pin)) != 4:
            return "❌ PIN must contain exactly 4 digits"

        if str(self.__pin).isdigit() == False:
            return "❌ PIN must contain only numbers"

        if len(set(str(self.__pin))) == 1:
            return "⚠️ Very Weak PIN"

        if str(self.__pin) in ["1234", "4321", "1111", "0000"]:
            return "⚠️ Weak PIN - Easy to guess"

        return "✅ Strong PIN"


    # Public method to check the PIN
    def check_safety(self):
        self.__status = self.__check_pin()
        print("🔎 PIN Safety Result:", self.__status)


    # 🔑 Setter method to safely update private PIN
    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("🔄 PIN has been updated successfully!")


    # Public method to show account information
    def show_account(self):
        print("\n👤 Account Name :", self.name)
        print("🔐 PIN Status   :", self.__status)


    # ⭐ Special __str__ function
    def __str__(self):
        return "🔐 Smart Account of " + self.name


# -----------------------------------------
# 🚀 Create Account Object
# -----------------------------------------

account = Account("Alex", 1234)

print(account)

print("\n===== FIRST PIN CHECK =====")
account.check_safety()

account.show_account()


# -----------------------------------------
# 🧪 Testing private variable
# -----------------------------------------

print("\n===== TESTING PRIVATE DATA =====")

account.__pin = 9876

print("Tried changing private PIN directly to 9876.")
print("But the real private PIN is still protected! 🔒")


# -----------------------------------------
# 🔄 Updating PIN using Setter
# -----------------------------------------

print("\n===== UPDATING PIN =====")

account.set_pin(7392)

account.check_safety()
account.show_account()


# -----------------------------------------
# 🎉 Final Result
# -----------------------------------------

print("\n================================")
print("🎉 ACCOUNT SECURITY CHECK DONE!")
print("================================")