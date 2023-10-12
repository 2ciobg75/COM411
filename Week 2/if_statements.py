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