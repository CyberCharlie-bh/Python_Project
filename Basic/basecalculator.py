from contextlib import _BaseExitStack
while True:
    print("Hello And Welcome to my basic Calculator")

    a = int(input("Enter the first number: - "))

    b = int(input("Enter the second number: - "))

    c = input("Enter the required opertion: - ")

    operators = ["+","-","/","*"]

    while c in operators:
        if c == "+":
            print("The Answer is:",(a+b))

        elif c == "-":
            print("The Answer is:",(a-b))

        elif c == "/":
            print("The Answer is:",(a/b))

        elif c == "*":
            print("The Answer is:",(a*b))

        else:
            print("How the fuck you reached here")
        break

    y = input("Do you want to continue yes or no: -  ")

    if y == "no":
        break
    else:
        pass
    print("It works")

print("Thanks For Trying my Project")
