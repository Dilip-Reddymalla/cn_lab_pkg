"""
Dummy Server module for cn_lab package.
"""
import socket
import sys

def run_dummy_server(host="0.0.0.0", port=12345):
    """Start an echo/chat server listening for client connections."""
    print(f"[Dummy Server] Starting on {host}:{port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((host, port))
            server_socket.listen(1)
            print(f"[Dummy Server] Listening on {host}:{port}... Waiting for client connection.")
            conn, addr = server_socket.accept()
            with conn:
                print(f"[Dummy Server] Connected by {addr}! (Type 'bye' to exit)")
                while True:
                    msg = conn.recv(1024).decode()
                    if not msg or msg.lower().strip() == "bye":
                        print("[Dummy Server] Client disconnected.")
                        break
                    print(f"Client: {msg}")
                    reply = input("Server: ")
                    conn.send(reply.encode())
                    if reply.lower().strip() == "bye":
                        print("[Dummy Server] Server closed chat.")
                        break
    except KeyboardInterrupt:
        print("\n[Dummy Server] Server stopped.")

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 12345
    run_dummy_server(port=port)

if __name__ == "__main__":
    main()

