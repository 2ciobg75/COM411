# Ask the user for a special character
print("Program Started!")

print("Please enter a standard character: ")
letter = input()

# Check to see if the user entered one character
if len(letter) == 1:
    print(f"The ASCII code for {letter} is {ord(letter)}")
else:
    print("You need to enter one character")

print("Program Ended!")
