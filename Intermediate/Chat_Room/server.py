import socket

Host = "127.0.0.1"
Port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((Host, Port))
server.listen(2)

print("Waiting for the client")
client_socket ,address = server.accept()

print(f'The client is connected {client_socket}')
print("Client connected")

while True:
    data = client_socket.recv(1024).decode()
    if not data:
        print("Client disconnected")
        break

    print(f'Client says:',data)
    
    if data.lower() in ["bye server","bye","quit"]:
        break
    else:
        pass

    reply = input("What do u wanna reply:- ")
    client_socket.send(reply.encode())

client_socket.close()
server.close()
print("Server closed")
