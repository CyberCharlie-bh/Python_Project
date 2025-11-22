# This does not contain threading method

import socket

HOST = input("Please enter the IP address:- ")
PORT1 = int(input("Please enter the port start scan from:- "))
PORT2 = int(input("Please enter the port end scan at:- "))
print(f'Scanning {HOST} between {PORT1} and {PORT2}')

for PORT in range(PORT1,(PORT2+1)):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)

    Connect = client.connect_ex((HOST,PORT))

    if Connect == 0:
        print(f'{PORT} is open')

    else:
        print(f'{PORT} is closed (Error: {Connect})')
    client.close()
