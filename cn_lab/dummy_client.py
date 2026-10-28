"""
Dummy Client module for cn_lab package.
"""
import socket
import sys

def run_dummy_client(host="127.0.0.1", port=12345):
    """Connect to a server, send messages, and receive replies."""
    print(f"[Dummy Client] Connecting to {host}:{port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"[Dummy Client] Connected to {host}:{port}! (Type 'bye' to exit)")
            while True:
                msg = input("Client: ")
                client_socket.send(msg.encode())
                if msg.lower().strip() == "bye":
                    print("[Dummy Client] Exited.")
                    break
                reply = client_socket.recv(1024).decode()
                if not reply or reply.lower().strip() == "bye":
                    print("[Dummy Client] Server ended connection.")
                    break
                print(f"Server: {reply}")
    except ConnectionRefusedError:
        print(f"[Dummy Client] Connection refused. Is the server running on {host}:{port}?")
    except KeyboardInterrupt:
        print("\n[Dummy Client] Stopped by user.")

def main():
    host = sys.argv[1] if len(sys.argv) > 1 else input("Enter Server IP [127.0.0.1]: ").strip() or "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 12345
    run_dummy_client(host, port)

if __name__ == "__main__":
    main()

