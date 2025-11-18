while True:
    print("Hello And Welcome to my basic Calculator")

    a = int(input("Enter the first number: - "))

    b = int(input("Enter the second number: - "))

    c = input("Enter the required opertion: - ")

    operators = ["+","-","/","*"]
    
    def addition():
        return a+b

    def multiply():
        return a*b
    
    def subtract():
        return a-b
    
    def divsion():
        return a/b

    
    if c in operators:

        if c == "+":
            print("The Answer is:",addition())

        elif c == "-":
            print("The Answer is:",subtract())

        elif c == "/":
            print("The Answer is:",divsion())

        elif c == "*":
            print("The Answer is:",multiply())

        else:
            print("How the fuck you reached here")
        
    else:
        print("Wrong operation")

    y = input("Do you want to continue yes or no: -  ")

    if y == "no":
        break
    else:
        pass

print("Thanks For Trying my Project")
