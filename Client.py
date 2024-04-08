# client.py

import socket
import threading

def test():
    print("Hello")

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break  # Server disconnected
            print(f"Received from server: {data}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def start_client():
    host = input("Enter the recipents IP")
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode())

if __name__ == "__main__":
    start_client()
