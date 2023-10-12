#Ask user to enter their name
print("What is your name?")
name = str(input())

#Ask the user for their age
print("How old are you (in years)?")
age = int(input())

#Ask the user for their height
print("How tall are you (in meters)?")
height = float(input())

#Ask the user for their weight
print("How much do you weigh (in kilograms)?")
weight = float(input())

#Calculation of BMI
BMI = weight/height**2

#Display the result
print(f"{name} you are {age} years old and you BMI is {BMI:.2f}")

#Ask for user inputs
print("Please enter the number of lives: ")
lives = int(input())

print("Please enter the energy level: ")
energy = int(input())

print("Please enter the shield level: ")
shield = int(input())

#Print the results
print("Stats have been set. \n")
print("Lives:" + lives * "❤")
print("Energy: " + energy * "❖")
print("Shield: " + shield * "❖")