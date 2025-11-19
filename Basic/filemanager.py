import os

# R = Read
# A = Append
# W = Write
# X = Create


while True:

    print("We have two build in operation in this file manager program\nCreate\nDelete")

    i = str(input("What type of operation do you want to do:- "))

# --------------------- Creation of A Text File ------------------------------

    if i == "create" or i == "Create":
    
        x = str(input("Write the name of file u want to create:- "))
    
        w = input("Write the contents:- ")

        if not os.path.exists(x):

            with open(x , "w") as file:
                file.write(w)
                print("File created")

        else:
    
            print("file exists")

# ----------------------- Deletion of File ---------------------------------------

    elif i == "delete" or i == "Delete":
    
        d = str(input("Write the name of file u want to delete:- "))
        sure = str(input("Are you sure yes or no:- "))

        if sure == "yes":

            if os.path.exists(d):
                os.remove(d)
                print("File have been deleted")

            else:
                print("File doesnt exists")

        else:
            print("Ok Please check the file before continue")

    else:
        print("Wrong operation")
        print("Please type create and delete on operation")

# -------------------- continue -------------------------------------

    y = input("Do you want to continue yes or no: -  ")

    if y == "no":
        break
    else:
        pass

print("Thanks for trying my project")
