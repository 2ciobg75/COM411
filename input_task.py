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
