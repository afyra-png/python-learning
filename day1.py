#1. hello you!
user_name = input("What's your name? > ")

print(f"Hello, {user_name}! Hope you're having a good day!")

#2. even or odd
while True:
    try:
        number = int(input("enter a number > ")) 
        if not number:
            if number % 2 == 0:
                print("the number is even")
            else:
                print("the number is odd")
        break

    except ValueError:
        print("That's not a valid NUMBER")      

#3. calculator
numbers = input("Put two numbers and an operation here: ")
pass
print("The result is {}")
pass

#4. age checker 
try:
    age = int(input("What's you age bbg? > "))
except ValueError:
    print("Age in numbers duh")

if age < 13:
    print("You're a kiddo")
elif age >= 13 >= 17:
    print("You're a teennn")
else:
    print("You're an adult ass")

#5. temperature converter
celcius = input("Enter a temperature in Celcius here: ")

fahrenheit = float((celcius * 1.8) + 32)

print(f"The temperature in Fahrenheit is {fahrenheit}°F")

#6. BMI calculator
weight = input("WHAT'S YOUR WEIGHT?? (in kg) > ")
weight = float(weight)

height = input("WHAT'S YOUR HEIGHT THEN?? (in m) > ")
height = float(height)

bmi = weight / height*height

if bmi < 18.5:
    print("You're underweight smh")
elif bmi >= 18.5 <= 24.9:
    print("You're healthy alhamdulillah")
elif bmi >= 25.0 <= 29.9:
    print("You're overweight wallahu")
else:
    print("SMH YOU NEED TO LOSE SOME FATASS (YOU'RE OBESE)")





