print("📚 ===== Dictionary Frequency Checker ===== 📚")

# Empty Dictionary
test_dict = {}

# Number of entries
n = int(input("🔢 How many words do you want to enter? : "))

# Taking input
for i in range(n):
    print(f"\n📝 Entry {i + 1}")
    key = input("🔑 Enter word: ")
    value = int(input("🔢 Enter value: "))
    test_dict[key] = value

# Display Dictionary
print("\n📖 Your Dictionary is:")
print(test_dict)

# Value to search
K = int(input("\n🎯 Enter the value to check frequency: "))

count = 0

# Counting frequency
for key in test_dict:
    if test_dict[key] == K:
        count += 1

# Display Result
print("\n📊 Result")
print("✅ Frequency of", K, "is:", count)

print("\n🎉 Thank you for using Dictionary Frequency Checker! 😊")