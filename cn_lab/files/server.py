import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "0.0.0.0"
port = 12345

server_socket.bind((server_ip, port))
server_socket.listen(1)
print(f"Server is listening on port {port}...")

conn, addr = server_socket.accept()
print(f"Connected with client {addr}")

while True:
    msg = conn.recv(1024).decode()
    if msg.lower() == "bye":
        print("Client ended chat.")
        break

    print(f"Client: {msg}")
    reply = input("Server: ")
    conn.send(reply.encode())
    if reply.lower() == "bye":
        print("Server ended chat.")
        break

conn.close()
server_socket.close()
