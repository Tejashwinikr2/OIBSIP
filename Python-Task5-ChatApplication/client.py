import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter your username: ")


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "USERNAME":
                client.send(username.encode())
            else:
                print(message)

        except:
            print("Disconnected from the server.")
            client.close()
            break


def send_messages():
    while True:
        try:
            message = input()

            if message.lower() == "exit":
                client.send("exit".encode())
                client.close()
                break

            formatted_message = f"{username}: {message}"
            client.send(formatted_message.encode())

        except:
            break


receive_thread = threading.Thread(
    target=receive_messages,
    daemon=True
)

send_thread = threading.Thread(
    target=send_messages,
    daemon=True
)

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()
