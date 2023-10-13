# Ask the user how many apples they want to remove
print("How many apples should I remove?")
apples_numb = int(input())

#  The robot will remove the number of apples specified above
print(f"I will remove {apples_numb} apples.")
while apples_numb != 0:
    apples_numb = apples_numb - 1
    print("Removed one apple.")

# Ask the user how many obstacles should the robot avoid
print("How many obstacles must I avoid?")
obstacles_numb = int(input())
obstacles_var = 0

# Count the number of obstacles avoided
print(f"I will avoid {obstacles_numb} obstacles!")
while obstacles_numb != obstacles_var:
    obstacles_var = obstacles_var + 1
    print(f"Avoiding...Done! {obstacles_var} obstacles avoided.")
print("\n All obstacles have been avoided")