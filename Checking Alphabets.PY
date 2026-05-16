# ==========================================
#      Alphabet Checker Mini Project
# ==========================================

print("===================================")
print("      WELCOME TO ALPHABET CHECKER ")
print("===================================")

# Taking input from the user
ch = input("Enter any single character: ")

# Checking the length of input
if len(ch) != 1:
    print(" Please enter only ONE character.")
else:
    
    # Checking whether the character is an alphabet
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        
        print("\n RESULT")
        print("-------------------")
        print(ch, "is an ALPHABET ")
        
        # Extra feature
        if 'A' <= ch <= 'Z':
            print("It is an UPPERCASE letter.")
        else:
            print("It is a LOWERCASE letter.")
    
    else:
        print("\n RESULT")
        print("-------------------")
        print(ch, "is NOT an alphabet ")

print("\nThank you for using Alphabet Checker!")