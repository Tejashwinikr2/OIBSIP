import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

clients = []
usernames = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server started on {HOST}:{PORT}")
print("Waiting for clients...")


def timestamp():
    return datetime.now().strftime("%H:%M:%S")


def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                remove_client(client)


def remove_client(client):
    if client in clients:
        index = clients.index(client)
        username = usernames[index]

        clients.remove(client)
        usernames.remove(username)

        try:
            client.close()
        except:
            pass

        message = f"[{timestamp()}] {username} disconnected."
        print(message)
        broadcast(message.encode())


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                remove_client(client)
                break

            text = message.decode()

            if text.lower() == "exit":
                remove_client(client)
                break

            print(text)
            broadcast(message, client)

        except:
            remove_client(client)
            break


def receive_connections():
    while True:
        client, address = server.accept()

        client.send("USERNAME".encode())
        username = client.recv(1024).decode()

        clients.append(client)
        usernames.append(username)

        print(f"[{timestamp()}] {username} connected from {address}")

        welcome = f"[{timestamp()}] {username} joined the chat."
        broadcast(welcome.encode(), client)

        client.send(
            f"[{timestamp()}] Connected to the chat server.".encode()
        )

        thread = threading.Thread(
            target=handle_client,
            args=(client,),
            daemon=True
        )
        thread.start()


receive_connections()
