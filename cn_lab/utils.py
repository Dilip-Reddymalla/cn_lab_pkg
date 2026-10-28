"""
Utility helper functions for networking diagnostics.
"""
import socket

def get_local_ip():
    """Retrieve the primary local IP address of this machine."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"

def ping_host(host="127.0.0.1", port=80, timeout=2.0):
    """Check if a remote host/port is reachable via TCP."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

