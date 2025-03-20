import os
import socket
import hashlib
import random
import string

FILE_PATH = "/serverdata/randomtext.txt"

def generate_random_file():
    data = ''.join(random.choices(string.ascii_letters + string.digits, k=1024))
    with open(FILE_PATH, "w") as f:
        f.write(data)

def calculate_checksum():
    hasher = hashlib.md5()
    with open(FILE_PATH, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def start_server(host, port):
    generate_random_file()
    checksum = calculate_checksum()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server on {host}:{port}")
        print("Listening for incoming connections...")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            with open(FILE_PATH, "rb") as f:
                conn.sendall(f.read())
            conn.sendall(checksum.encode())

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python server.py <PORT>")
        sys.exit(1)
    start_server("0.0.0.0", int(sys.argv[1]))
