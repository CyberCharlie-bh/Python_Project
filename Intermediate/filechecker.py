# The file is checked with hash

import hashlib
import os

while True:
    print("Please know the hash of file from the website")
    print("The hash used is SHA-256")
    file_name = input("Please state the filename:- ")
    file_hash = input("Please state the hash:- ").lower()

    if os.path.exists(file_name):
        
        with open(file_name, "rb") as file:
        
            sha256_file = hashlib.sha256()
            
            while chunk := file.read(4096):
                sha256_file.update(chunk)

            hash_file = sha256_file.hexdigest().lower()
        
        if hash_file == file_hash:

            print(f'The file {file_name} has not tampered with and its intergrity is intact')

        else:

            print(f'The file {file_name} has been tampered with\nBut there are some errors')
            print("1.The given hash might be different from the website please copy paste them and recheck before submittiing")
            print(f'2.The filename {file_name} might be wrong from the website')

    else:

        print("File doesnt exists in this folder\nPlease go to that specific folder where it is")


    y = input("Do you want to continue yes or no: -  ")

    if y == "yes":
        pass
    else:
        break

print("Thanks For Trying my Project")
