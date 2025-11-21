import hashlib

while True:
    print("This project has 4 types of hash")
    print(f'A)MD5\nB)SHA-1\nC)SHA-256\nD)SHA-512')
    print("Please choose on A/B/C/D")

    hash = input("Please enter the hash type:- ").lower()
    word = input("Please enter the word you want to hash:- ")

    if hash == "a":

        biword = word.encode()
        md5_hash = hashlib.md5(biword)
        final_hash = md5_hash.hexdigest()
        print(f'The MD5 hash of the {word} is {final_hash}')

    elif hash == "b":

        biword = word.encode()
        sha1_hash = hashlib.sha1(biword)
        final_hash = sha1_hash.hexdigest()
        print(f'The SHA-1 hash of the {word} is {final_hash}')
    
    elif hash == "c":

        biword = word.encode()
        sha256_hash = hashlib.sha256(biword)
        final_hash = sha256_hash.hexdigest()
        print(f'The SHA-256 hash of the {word} is {final_hash}')
    
    elif hash == "d":

        biword = word.encode()
        sha512_hash = hashlib.sha512(biword)
        final_hash = sha512_hash.hexdigest()
        print(f'The SHA-512 hash of the {word} is {final_hash}')

    else:

        print("Incorrect Input Please choose A/B/C/D")


    y = str(input("Do you want to continue:- "))

    if y == "yes":
        pass
    else:
        break

print("Thanks For Trying my Project")
