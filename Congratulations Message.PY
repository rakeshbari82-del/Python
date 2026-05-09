print("1. Concatenation (Joining)")

#This merges strings using the + operator.

first = "Code"
second = "Editor"
print(first + "Result of Concatenation :  " + second)

print("2. Indexing and Slicing")

#Indexing grabs one character; slicing grabs a range (from start up to, but not including, end).

word = "Universe"
print("Word : Universe")
print( "Result of Indexing and Slicing : ", word[0])
print( "Result of Indexing and Slicing : ", word[0:3])

print("3. Finding Length")

#The len() function counts every character, including spaces.

text = "Hello!"
print( "Result of Finding Length : ",len(text))

print("4. Modifying Case")

#Use .upper() or .lower() to change the text's appearance.

name = "Eagle"
print("Result of Modifying Case Name Eagle in Upper is : ", name.upper())
print("Result of Modifying Case Name BOB in Lower is : ","BOB".lower())

print("5. Searching and Replacing")

#.find() tells you where a word starts, and .replace() swaps text out.

sentence = "I love cats."
print("Sentence : I love cats.")
print( "Result of Searching : ", sentence.find("cats"))       
print( "Result of Replacing : ", sentence.replace("cats", "dogs")) 

print("6. Splitting and Joining")

#.split() turns a string into a list, and .join() turns a list back into a string.

Colors = "Red,Blue,Green"
print("Colors : Red,Blue,Green")
print("Result of Splitting : ",Colors.split(","))
Colours = {"Red","Blue","Green"}
print("Result of Joining : ", "-".join(Colours))

print("7. Removing Whitespace")

#.strip() cleans up extra spaces at the beginning or end of a string.

user_input = "  password123  "
print("user_input =   password 1 2 3  ")
print("Result of Removing Whitespace : ", user_input.strip())