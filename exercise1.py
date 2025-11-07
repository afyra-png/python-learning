#LEVEL 1 
#1. postivie or negative
number = float(input("Please enter a number here: "))

if number < 0:
    print("The number is negative.")
elif number > 0:
    print("The number is poosaytive.")
else:
    print("The number is equal ZEROO")

#2. password check
password = "you're gay"

user_input = input("Enter the password: ")

if user_input == password:
    print("Correct password, you're in")
else:
    print("Incorrect password, try me bich")

#3. word length
word = input("Type a word: ")
length = len(word)
print(f"The length of your word is {length}.")

#4. temp convert
celcius = float(input("Enter a temperature in Celcius here: "))
fahrenheit = float((celcius * 1.8) + 32)
print(f"The temperature in Fahrenheit is {fahrenheit}°F.")

#5. count vowels
vowels = ["a","e","i","o","u"]
text = input("Write any sentence:")
count = 0

for letter in text:
    if letter.lower() in vowels:
        count += 1
print(f"There are {count} vowels in your sentence.")


