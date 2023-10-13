# Ask the user for the type of book
print("What type of book is this?")
book = input()

# Check to see if the user picked adventure
if book == "adventure":
    print("I like adventure books!")

print("Finished reading book.")

# Ask user if we are performing calculations
print("Please enter the activity to be performed.")
activity = input()

# Display either "performing calculations" or "performing activity"
if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing activity...")

print("Activity completed!")

# Give instructions to robot
print("Towards which direction should I go (up, down, left or right)?")
direction = input()

# The robot will move in the direction specified
if direction == "up":
    print("I am moving in an upward direction")
elif direction == "down":
    print("I am moving in an downward direction")
elif direction == "left":
    print("I am moving in an leftward direction")
elif direction == "right":
    print("I am moving in an rightward direction")
else:
    print("You didn't give me correct instructions.")

# Ask the user to enter a number
print("Please enter a number: ")
number = int(input())

if (number % 2) == 0:
    print(f"The {number} is even.")
else:
    print(f"The {number} is odd.")
