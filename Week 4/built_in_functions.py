# Ask the user for a special character
print("Program Started!")

print("Please enter a standard character: ")
letter = input()

# Check to see if the user entered one character
if len(letter) == 1:
    print(f"The ASCII code for {letter} is: {ord(letter)}")
else:
    print("You need to enter one character")

print("Program Ended!")

# Ask the user to enter some ASCII code
print("Program started!")

print("Please enter an ASCII code: ")
ascii_code = abs(int(input()))

# Check to see if the ascii code is between 32 and 126
if 32 <= ascii_code <= 126:
    print(f"The character represented by ASCII code {ascii_code} is: {chr(ascii_code)}")
else:
    print("Please enter a ASCII code from 32 to 126.")

print("Program Ended!")
