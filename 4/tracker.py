all_projects = []

while True:
    name = input("\nProject name (or type 'done' to see list): ")
    if name.lower() == 'done':
        break

    category = input("Category (School/Work/Hobby): ")
    hours = int(input("Total hours needed: "))
    days = int(input("Days left: "))

    project_entry = {
        "name": name,
        "cat": category,
        "daily": hours/days
    }
    all_projects.append(project_entry)

    print("\n--- DASHBOARD ---")
    for p in all_projects:
        status = "bru needa lock in" if p['daily'] > 5 else "bro is chill huh"

        print(f"[{p['cat']}] {p['name']}: {p['daily']:.1f} hrs/day - {status}")

        