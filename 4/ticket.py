tickets = []

while True :
    choice = input("\nChoose: buy / show / exit: ")

    if choice == "buy":
        name = input("What's your name? ")
        movie = input("What movie you want to watch? ")
        quantity = int(input("How many ticket you want to buy? "))

        ticket_list = {
            "name" : name,
            "movie": movie,
            "quantity": quantity
            }
        
        tickets.append(ticket_list)
        print("Thank you for your order!")
        
    elif choice == "show" :
        print("\nWelcome to your Dashboard")

        print(f"\nHere's your ordered ticket: ")
        for p in tickets: 
            print(f"Name: {p["name"]}")
            print(f"Movie: {p["movie"]}")
            print(f"Quantity: {p["quantity"]}\n")

    elif choice == "exit" : 
        break



        
