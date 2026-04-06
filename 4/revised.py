#deadline tracker
all_projects = [] #this list remembers everything user enter

project_data = {
    "name": "Design Portfolio",
    "category": "Work",
    "hours": 10
}

name = input("What project are you working on? ")
total_hours = int(input("How many total hours will this take? (numbers only) "))
days_left = int(input("How many days until the deadline? (numbers only) "))

hours_per_day = total_hours / days_left 

new_project = {
    "name": name,
    "hours": total_hours,
    "daily_rate": hours_per_day
}
all_projects.append(new_project)

print (f"To finish the {name} project, you need to work {hours_per_day:.2f} hours per day.")

if len(all_projects) > 8:
    print("ay bru yo list getting bit long ahh, take yo deep breathie, shawty might be lookin at an all nighter ahh shi ")


