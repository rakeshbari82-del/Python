try:
    num1, num2 = eval(input("Enter Two Numbers, Separated by a Comma : "))
    result = num1 / num2
    print("Result is ", result)
    

except ZeroDivisionError:
    print("Division by Zero is Error !!")

except SyntaxError:
    print("Comma is Missing. Enter Numbers Separated by Comma like this 1, 2")

except:
    print("Wrong Input")

else:
    print("No Exceptions")

finally:
    print("This will excute no matter what")