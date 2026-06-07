import turtle

# Screen setup
screen = turtle.Screen()
screen.title("✨ Magic Square Art Studio ✨")
screen.bgcolor("skyblue")

# Ask user for square size
size = int(input("Enter the size of the square: "))

# Create turtle
artist = turtle.Turtle()
artist.shape("turtle")
artist.speed(5)
artist.pensize(4)

# Draw decorative stars
artist.penup()
artist.goto(-200, 150)
artist.color("yellow")

for i in range(20):
    artist.dot(10)
    artist.forward(20)

# Move to drawing position
artist.goto(-size/2, size/2)
artist.pendown()

# Draw square
artist.color("darkblue")
artist.fillcolor("lightgreen")
artist.begin_fill()

for i in range(4):
    artist.forward(size)
    artist.right(90)

artist.end_fill()

# Draw a small square inside
artist.penup()
artist.goto(-size/4, size/4)
artist.pendown()

artist.color("red")
artist.fillcolor("pink")
artist.begin_fill()

for i in range(4):
    artist.forward(size/2)
    artist.right(90)

artist.end_fill()

# Write title
artist.penup()
artist.goto(-120, -size)
artist.color("purple")
artist.write(
    "🌟 My Creative Square 🌟",
    font=("Arial", 18, "bold")
)

# Hide turtle
artist.hideturtle()

turtle.done()