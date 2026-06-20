import turtle

# ==========================
# FACTORIAL FUNCTION
# ==========================

def factorial(n):
    """Recursive factorial function"""

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# ==========================
# FIBONACCI FUNCTION
# ==========================

def fibonacci(n):

    series = []

    a = 0
    b = 1

    for i in range(n):
        series.append(a)
        a, b = b, a+b

    return series

# ==========================
# TURTLE DESIGN
# ==========================

def draw_fibonacci():

    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Fibonacci Spiral Design")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(3)

    colors = [
        "red",
        "orange",
        "yellow",
        "green",
        "cyan",
        "blue",
        "purple",
        "pink"
    ]

    fib = fibonacci(12)

    for i in range(len(fib)):

        pen.pencolor(colors[i % len(colors)])

        length = fib[i] * 5

        pen.forward(length)
        pen.right(90)

    pen.hideturtle()

    turtle.done()

# ==========================
# MAIN MENU
# ==========================

while True:

    print("\n")
    print("="*40)
    print("     FACTORIAL & FIBONACCI LAB")
    print("="*40)

    print("1. Find Factorial")
    print("2. Fibonacci Series")
    print("3. Fibonacci Turtle Art")
    print("4. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        num = int(input("Enter Number : "))

        print()
        print("Factorial =", factorial(num))

    elif choice == "2":

        terms = int(input("Enter Number of Terms : "))

        print()

        fib = fibonacci(terms)

        print("Fibonacci Series")

        for i in fib:
            print(i)

    elif choice == "3":

        draw_fibonacci()

    elif choice == "4":

        print("Thank You")
        break

    else:
        print("Invalid Choice")