# Ask the user how many apples they want to remove
print("How many apples should I remove?")
apples_numb = int(input())

#  The robot will remove the number of apples specified above
print(f"I will remove {apples_numb} apples.")
while apples_numb != 0:
    apples_numb = apples_numb - 1
    print("Removed one apple.")

