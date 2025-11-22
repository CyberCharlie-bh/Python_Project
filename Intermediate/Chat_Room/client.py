import socket

HOST = ("127.0.0.1")
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))


while True:
    Input = input("Please state the data for server:- ")
    client.send(Input.encode())

    data = client.recv(1024).decode()
    print("Server says: ",data)
    
    if not data:
        print("Server discontinued")
        break

    if data.lower() in ["bye","bye client","quit"]:
        break
    else:
        pass

client.close()
