# server.py

import socket
import threading

clients = []  # List to store connected clients

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break  # Client disconnected
            print(f"Received from client: {data}")
            # Process the message (e.g., store in a database, etc.)
            # You can add more logic here
            # Broadcast the message to all connected clients
            for client in clients:
                client.send(data.encode())
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
