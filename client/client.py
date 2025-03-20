import socket
import hashlib

FILE_PATH = "/clientdata/receivedtext.txt"

def receive_file(server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_ip, server_port))
        data = b""
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            data += chunk

        received_checksum = data[-32:].decode()  # Extract last 32 bytes as checksum
        file_data = data[:-32]  # Remaining is the file data

        with open(FILE_PATH, "wb") as f:
            f.write(file_data)

        computed_checksum = hashlib.md5(file_data).hexdigest()
        
        if received_checksum == computed_checksum:
            print("File received successfully. Checksum verified!")
        else:
            print("File corruption detected!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python client.py <SERVER_IP> <PORT>")
        sys.exit(1)
    receive_file(sys.argv[1], int(sys.argv[2]))
