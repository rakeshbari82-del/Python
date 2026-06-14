# ==========================================
#      🔬 AVIKA'S CIRCLE SCIENCE LAB 🔬
# ==========================================

import math
import random
import turtle


# ------------------------------
# Function to Calculate Circumference
# ------------------------------
def calculate_circumference(radius):
    return 2 * math.pi * radius


# ------------------------------
# Function to Draw Circle
# ------------------------------
def draw_circle(radius):

    screen = turtle.Screen()
    screen.title("🔬 Avika's Circle Science Lab")
    
    # 🎨 Background Color
    screen.bgcolor("lightblue")

    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(4)
    pen.pensize(3)

    pen.color("yellow")
    pen.fillcolor("orange")

    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

    circumference = calculate_circumference(radius)

    pen.penup()
    pen.goto(0, -(radius + 30))
    pen.write(
        f"Radius = {radius}",
        align="center",
        font=("Arial", 12, "bold")
    )

    pen.goto(0, -(radius + 55))
    pen.write(
        f"Circumference = {circumference:.2f}",
        align="center",
        font=("Arial", 12, "bold")
    )

    turtle.done()


# ------------------------------
# Welcome Screen
# ------------------------------
print("=" * 65)
print("🎯 🔬 WELCOME TO AVIKA'S CIRCLE SCIENCE LAB 🔬 🎯")
print("=" * 65)

while True:

    print("\n📋 MAIN MENU")
    print("1️⃣  Calculate Circumference")
    print("2️⃣  Amazing Circle Facts")
    print("3️⃣  Draw Circle with Turtle")
    print("4️⃣  Exit")

    choice = input("\n👉 Enter your choice (1-4): ")

    # -----------------------------------
    # Option 1 : Circumference Calculator
    # -----------------------------------
    if choice == "1":

        try:
            radius = float(input("\n📏 Enter Radius: "))

            if radius < 0:
                print("❌ Radius cannot be negative!")
                continue

            circumference = calculate_circumference(radius)

            print("\n" + "=" * 45)
            print("✨ CIRCLE REPORT ✨")
            print("=" * 45)

            print(f"🔵 Radius         : {radius}")
            print(f"⭕ Circumference  : {circumference:.2f}")

            if radius < 5:
                print("😊 Small Circle")
            elif radius < 15:
                print("😎 Medium Circle")
            else:
                print("🚀 Giant Circle")

            print("\n🎉 Calculation Completed Successfully!")

        except ValueError:
            print("❌ Please enter a valid number!")

    # -----------------------------------
    # Option 2 : Fun Facts
    # -----------------------------------
    elif choice == "2":

        facts = [
            "🌎 Earth appears almost circular when viewed from space.",
            "⚽ Most sports balls are based on circular shapes.",
            "🎡 Ferris wheels are giant circles.",
            "🪙 Coins are circular because they wear evenly.",
            "⌚ Most clocks use a circular shape.",
            "🚴 Bicycle wheels are circular for smooth movement.",
            "🍕 Pizzas are usually circular for even cooking.",
            "🌕 The Moon appears circular in the sky.",
            "☀️ The Sun looks like a giant circle.",
            "💍 Rings have no beginning and no end.",
            "🎯 Dartboards are circular for fair scoring.",
            "🎪 Circus rings are circular for better viewing.",
            "🛞 Car tires are circular for efficient travel.",
            "🧭 Compasses help draw perfect circles.",
            "📀 CDs and DVDs are circular for smooth spinning.",
            "🌀 A circle has no corners.",
            "📐 Every point on a circle is equally distant from the center.",
            "🤯 A circle has 360 degrees.",
            "⭐ Circumference is the distance around a circle.",
            "🔵 Pi (π) is an infinite number used in circle calculations.",
            "🎨 Artists use circles to create balance in designs.",
            "🏀 Basketball hoops are circular.",
            "🌈 Rainbows form full circles from above.",
            "🚀 Planets are nearly spherical because of gravity.",
            "🐢 Turtle Graphics can easily draw circles using Python!"
        ]

        print("\n" + "=" * 55)
        print("💡 AMAZING CIRCLE FACT")
        print("=" * 55)

        print(random.choice(facts))

        print("=" * 55)
        print(f"📚 Total Facts Available: {len(facts)}")

    # -----------------------------------
    # Option 3 : Turtle Drawing
    # -----------------------------------
    elif choice == "3":

        try:
            radius = int(input("\n🎨 Enter Radius to Draw: "))

            if radius <= 0:
                print("❌ Radius must be greater than 0!")
                continue

            print("🐢 Opening Turtle Graphics Window...")
            draw_circle(radius)

        except ValueError:
            print("❌ Please enter a valid number!")

    # -----------------------------------
    # Exit
    # -----------------------------------
    
    elif choice == "4":

        print("\n👋 Thank you for visiting Avika's Circle Science Lab!")
        print("🌟 Keep Learning Python!")
        print("🚀 Future Scientist in Action!")
        break

    # -----------------------------------
    # Invalid Input
    # -----------------------------------
    else:
        print("❌ Invalid Choice! Please select 1-4.")