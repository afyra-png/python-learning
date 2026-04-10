#deadline tracker

#1. ask for the project name 
project = input("What project are you working on? ")

#2. ask for the total hours needed (use int() here)
total_hours = int(input("How many total hours will this take? (numbers only) "))

#3. ask for the days remaining
days_left = int(input("How many days until the deadline? (numbers only) "))

#4. calculate hours per day
hours_per_day = round(total_hours / days_left, 2) #rounding 2 decimal places

#5.print the result using an f-string
print (f"To finish the {project} project, you need to work {hours_per_day.2f} hours per day.")