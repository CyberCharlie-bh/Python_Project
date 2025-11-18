import random
import string

while True:
    alphab = list(string.ascii_letters)
    digits = list(string.digits)

    special = ["@","#","$","%","&"]

    p = int(input("What are the numbers of passwords u need:- "))

    a = int(input("What are the numbers of aplhabets u need:- "))

    n = int(input("How many numbers do u need in passwords:- "))

    for i in range(p):
        if (a + n + 1) >= 8:
            
            password = (random.choices(digits, k=n) + random.choices(alphab, k=a) + random.choices(special))

            random.shuffle(password)

            main_password = (''.join(password))

            print(f'The password{i+1} is {main_password}')

        else:
            print("The password should be more than 8 characters please choose the characters accordingly")
            break
     
    try:
        y = str(input(f'Do you want to continue yes or no:-  \n'))

        if y == "no":
            break
        
        elif y == "yes":
            pass

        else:
            break

    except ValueError:
        
        print("Error Found")
        break




    

