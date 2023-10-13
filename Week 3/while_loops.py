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

# Ask the user how many bars should be charged
print("How many bars should be charged?")
bars_numb = int(input())
bars_var = 0

# The program will update with the number of charged bars
while bars_numb != bars_var:
    bars_var = bars_var + 1
    print("Charging:", bars_var * "█ ")

print("The battery is fully charged!")

# Ask the user to enter a phrase
print("Please enter a phrase: ")
user_phrase = input()
number_characters = 0
print(user_phrase)

# Count how many characters the phrase contains and display "Hi" that many times
while number_characters != len(user_phrase):
    number_characters = number_characters + 1
print("Hi " * number_characters)

# Program that counts the first 100 numbers
print("Calculating the sum of the first 100 numbers...")
numbers = 0
result_number = 0

while numbers != 100:
    numbers = numbers + 1
    result_number = result_number + numbers
print("...Done! The answer is", result_number)
