# ╔══════════════════════════════════════════════════════╗
#        🌈✨ SUPER SMART ALPHABET ANALYZER ✨🌈
# ╚══════════════════════════════════════════════════════╝

print("🌟━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🌟")
print("🤖        WELCOME TO THE ALPHABET WORLD        🤖")
print("🌟━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🌟")

# Taking input from user
ch = input("\n🪄 Enter any single symbol to begin: ")

print("\n🔍 Initiating Smart Scan...")
print("⚡ Processing your input ⚡")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# Checking input length
if len(ch) != 1:
    print("🚫 OOPS! Invalid Input Detected 🚫")
    print("📢 Please enter ONLY one symbol at a time.")
    print("🎯 Example Inputs → A , z , 7 , @")

# Uppercase alphabet check
elif 'A' <= ch <= 'Z':
    print(f"🟢 SUCCESS! '{ch}' is an ALPHABET 🎓")
    print("🔠 Category      ➜ UPPERCASE LETTER")
    print("🧾 ASCII Value   ➜", ord(ch))
    print("👑 Awesome! You entered a CAPITAL letter.")
    print("🚀 Keep Exploring the Alphabet Galaxy!")

# Lowercase alphabet check
elif 'a' <= ch <= 'z':
    print(f"🟢 SUCCESS! '{ch}' is an ALPHABET 🎓")
    print("🔡 Category      ➜ LOWERCASE LETTER")
    print("🧾 ASCII Value   ➜", ord(ch))
    print("🌸 Cool! You entered a small letter.")
    print("💫 Learning Python is fun!")

# Number check
elif '0' <= ch <= '9':
    print(f"🔢 ALERT! '{ch}' is a NUMBER.")
    print("❌ Numbers are not alphabets.")
    print("📚 Try entering letters from A-Z or a-z.")

# Space check
elif ch == " ":
    print("⬜ WHOOPS! You entered a SPACE.")
    print("⚠️ Space cannot be counted as an alphabet.")
    print("🎈 Please try another symbol.")

# Special symbol check
else:
    print(f"💥 '{ch}' is a SPECIAL SYMBOL ⚡")
    print("🛑 Special symbols are not alphabets.")
    print("🎭 Examples ➜ @  #  $  %  &  *")
    print("🧠 Python successfully identified your input!")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("💖 Thank You for Using Smart Alphabet Analyzer")
print("🌟 Keep Coding • Keep Learning • Keep Growing 🌟")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")