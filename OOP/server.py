
import socket
import threading

# Server configuration
host = '127.0.0.1'
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

print(f"[*] Listening on {host}:{port}")

# List to hold client connections
clients = []

# Function to handle client connections
def handle_client(client_socket, addr):
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    while True:
        # Wait for data
        msg = client_socket.recv(1024).decode('utf-8')
        if not msg:
            break
        print(f"Received message from {addr[0]}:{addr[1]}: {msg}")

        # Broadcast message to all clients
        broadcast(msg, client_socket)

    # Remove client from list and close the connection
    clients.remove(client_socket)
    client_socket.close()

# Function to broadcast messages to all clients
def broadcast(msg, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client.send(msg.encode('utf-8'))
            except:
                clients.remove(client)

# Accept incoming connections
while True:
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)

    # Start a thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
