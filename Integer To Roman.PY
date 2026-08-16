# 🏛️ ROMAN NUMERAL MISSION 🚀
# Integer to Roman using Object-Oriented Programming


# PART 1: Create a class
class RomanConverter:

    # PART 2: Method to convert integer to Roman numeral
    def convert_to_roman(self, number):

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""

        # Convert number into Roman numeral
        for i in range(len(values)):
            while number >= values[i]:
                roman += symbols[i]
                number -= values[i]

        return roman


# PART 3: Create an object
converter = RomanConverter()


# PART 4: Welcome message
print("=" * 45)
print("🏛️  ROMAN NUMERAL MISSION  🏛️")
print("=" * 45)
print("🔢 Convert Integers into Roman Numerals!")
print("📌 Enter a number from 1 to 3999")
print("❌ Enter 0 to exit")
print("=" * 45)



# PART 5: Main program
while True:

    try:
        number = int(input("\n🔢 Enter an integer: "))

        # Exit option
        if number == 0:
            print("\n👋 Mission completed!")
            print("🏛️ Thank you for using Roman Numeral Mission!")
            break

        # Check valid range
        if number < 1 or number > 3999:
            print("⚠️ Please enter a number between 1 and 3999.")
            continue

        # Call the method
        result = converter.convert_to_roman(number)

        # Display result
        print("\n" + "-" * 45)
        print("🎯 CONVERSION RESULT")
        print("-" * 45)
        print("🔢 Integer       :", number)
        print("🏛️ Roman Numeral :", result)
        print("-" * 45)

    except ValueError:
        print("❌ Invalid input! Please enter a whole number.")