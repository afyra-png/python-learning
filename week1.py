#simple calculator 
#define all functions (+,-,*,/)
def add(num1, num2):
    return num1 + num2

def substract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

#ask user input
print("\n--- Simple Calculator ---")
#def structure and arguments
#structure: the syntax is def function_name(parameter1, parameter2, ...):

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Enter operation (add, substract, multiply, divide): )").lower()

    if operation == "add":
        result = add(num1, num2)
        print(f"Result: {result}.")
    
    elif operation == "substract":
        result = substract(num1,num2)
        print(f"Result: {result}")

    elif operation == "multiply":
        result = multiply(num1,num2)
        print(f"Result: {result}")
    
    elif operation == "divide":
        result = divide(num1,num2)
        print(f"Result: {result}")
    else:
        print("Error: Please enter only valid operations.")

except ValueError:
    print("Error: Please enter only valid numbers.")

#"real" calculator: the continuous mode
current_result = 0.0

while True:
    num1 = float(input("What you wanna count today: "))
    
    if user_input == "exit":
            break
        elif operation == "/":

except ZeroDivisionError:
    print("Error: Please input valid numbers.")

#number guess game

#import random

#def check_guess(user, correct):

#to do list

#list tasks = []

#add_task():
