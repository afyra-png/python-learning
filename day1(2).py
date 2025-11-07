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
        
    
