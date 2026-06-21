# ==============================================
#        🛒 SMART BILL PAYMENT SYSTEM 🛒
#        💳 Customer Due Amount Calculator 💳
# ==============================================

print("🌟" + "="*50 + "🌟")
print("         🛒 WELCOME TO SMART MART 🛒")
print("      💖 Fast • Easy • Secure Billing 💖")
print("🌟" + "="*50 + "🌟")

# Customer Details
name = input("\n👤 Enter Customer Name : ")

print("\n🛍️ Billing Section")
bill = float(input("💰 Enter Total Bill Amount (₹): "))
paid = float(input("💵 Enter Paid Amount (₹): "))

print("\n⏳ Calculating Your Bill...")

# Due Amount Calculation
due = bill - paid

print("\n" + "="*50)

if due > 0:
    print("📋 BILL SUMMARY")
    print("👤 Customer :", name)
    print("💰 Total Bill : ₹", bill)
    print("💵 Paid Amount : ₹", paid)
    print("❌ Due Amount : ₹", due)
    print("⚠️ Please pay the remaining amount soon.")
    print("🙏 Thank You for Shopping with Us!")

elif due == 0:
    print("📋 BILL SUMMARY")
    print("👤 Customer :", name)
    print("💰 Total Bill : ₹", bill)
    print("💵 Paid Amount : ₹", paid)
    print("✅ Payment Successful!")
    print("🎉 No Due Amount.")
    print("😊 Thank You! Visit Again.")

else:
    change = abs(due)
    print("📋 BILL SUMMARY")
    print("👤 Customer :", name)
    print("💰 Total Bill : ₹", bill)
    print("💵 Paid Amount : ₹", paid)
    print("💸 Extra Paid : ₹", change)
    print("🎁 Return Change : ₹", change)
    print("😊 Thank You! Have a Wonderful Day!")

print("="*50)

# Customer Rating
print("\n⭐ Rate Our Service")
print("1️⃣ ⭐")
print("2️⃣ ⭐⭐")
print("3️⃣ ⭐⭐⭐")
print("4️⃣ ⭐⭐⭐⭐")
print("5️⃣ ⭐⭐⭐⭐⭐")

rating = input("Enter Rating (1-5): ")

if rating == "5":
    print("🥰 Wow! Thank you for your 5-Star Rating!")
elif rating == "4":
    print("😊 Thank you! We hope to earn 5 Stars next time.")
elif rating == "3":
    print("🙂 Thanks! We'll improve our service.")
elif rating == "2":
    print("😔 Sorry! We'll do better.")
elif rating == "1":
    print("🙏 We apologize. Thank you for your feedback.")
else:
    print("⚠️ Invalid Rating!")

print("\n🎉 Program Completed Successfully!")
print("💖 Have a Nice Day,", name + "!")
print("🚀 Keep Smiling & Keep Coding!\n")