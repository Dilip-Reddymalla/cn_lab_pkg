import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input("Enter Server IP Address: ")
port = 12345
client_socket.connect((server_ip, port))
print(f"Connected to server {server_ip}:{port}")

while True:
    msg = input("Client: ")
    client_socket.send(msg.encode())

    if msg.lower() == "bye":
        print("Client ended chat.")
        break

    reply = client_socket.recv(1024).decode()
    if reply.lower() == "bye":
        print("Server ended chat.")
        break

    print(f"Server: {reply}")

client_socket.close()
