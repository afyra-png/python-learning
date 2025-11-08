#dice roller 

import random

dice = int(input("How many dice you want to roll? > "))
sides = int(input("How many sides each dice has? > "))

total = 0

for i in range(dice):
    result = random.randint(1,sides)
    print(f"Dice {i+1}: {result}.")
    total += result

print(f"The number of the dice is {total}.")
