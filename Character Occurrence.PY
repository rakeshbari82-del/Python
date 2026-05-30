string = input("Please Enter your own word : ")

char = input("Please Enter your own Character : ")

i = 0

count = 0

while(i < len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1

print("The Total Number Of Times ", char, "has Occurred = ", count)