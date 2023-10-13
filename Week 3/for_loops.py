# Ask the user how many times he wants to display a mountain
print("How many mountains should I display?")
numb_mountains = int(input())
print("I will display", numb_mountains, "mountains")
print("Displaying... \n")

# Code to display the number of mountains specified
for count in range(numb_mountains):
    print("     __")
    print("    /  \_")
    print("   /^    \ ")
    print("  /  ^    \_")
    print("_/ ^ ^     ^\ ")
    print("/  ^     ^    \ ")
