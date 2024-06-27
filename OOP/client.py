import socket
import threading

# Client configuration
host = '127.0.0.1'
port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Function to send messages to the server
def send_msg():
    while True:
        msg = input()
        client_socket.send(msg.encode('utf-8'))

# Function to receive messages from the server
def recv_msg():
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            print(msg)
        except:
            print("Connection closed")
            break

# Start sending and receiving threads
send_thread = threading.Thread(target=send_msg)
recv_thread = threading.Thread(target=recv_msg)

send_thread.start()
recv_thread.start()
