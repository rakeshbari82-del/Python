Amount = int(input("Please Enter Amount for Withdraw : "))

Note_1 = Amount//100
Note_2 = (Amount%100)//50
Note_3 = ((Amount%100)%50)//10

print("Notes of 100 rupee", Note_1)
print("Notes of 50 rupee", Note_2)
print("Notes of 10 rupee", Note_3)