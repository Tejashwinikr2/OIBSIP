# Chat Application

## Overview

Chat Application is a Python-based real-time messaging application that allows two users to communicate through a server using local network sockets.

The project demonstrates basic client-server communication, socket programming, threading, timestamps, and graceful disconnection handling.

## Features

- Client-server architecture
- Two-user real-time messaging
- Bidirectional message exchange
- Timestamp displayed with each message
- Multiple clients can connect to the server
- Graceful client disconnection handling
- Runs locally using `localhost`
- Simple command-line interface

## Technologies Used

- Python 3
- Socket Programming
- Threading
- `datetime`

## Project Structure

```text
Python-Task5-ChatApplication/
│
├── server.py
├── client.py
└── README.md
File Description
File
Purpose
server.py
Starts the server, accepts client connections, and manages message communication
client.py
Connects to the server and allows users to send and receive messages
README.md
Project documentation
How It Works
The application follows a client-server architecture:
Plain text
Server
                |
        -----------------
        |               |
     Client 1        Client 2
        |               |
        --------Chat-------
The server listens for incoming client connections. Each connected client is handled using a separate thread so that messages can be sent and received simultaneously.
Requirements
Python 3.x
No external Python packages are required.
How to Run
1. Start the Server
Open a terminal inside the project folder and run:
Bash
python server.py
The server will start listening for client connections.
2. Start Client 1
Open another terminal and run:
Bash
python client.py
Enter a username when prompted.
3. Start Client 2
Open a third terminal and run:
Bash
python client.py
Enter another username.
4. Start Chatting
Messages sent from one client will be received by the other connected client.
Each message is displayed with a timestamp.
Example:
Plain text
[14:35:20] Teju: Hello!
[14:35:25] Friend: Hi!
5. Disconnect
Type:
Plain text
exit
to leave the chat gracefully.
Features Demonstrated
Socket Communication
The project uses Python's socket module to establish communication between the server and clients.
Threading
The threading module allows the server to handle multiple connected clients simultaneously.
Timestamped Messages
Each message is displayed with the current time using Python's datetime module.
Graceful Disconnection
When a client disconnects, the server detects the disconnection and informs the remaining connected clients.
Security Note
This project is intended for learning and demonstration purposes. Messages are transmitted through local socket connections and are not end-to-end encrypted.
Future Enhancements
Graphical user interface using Tkinter
User authentication
Private messaging
Multiple chat rooms
Message history
Emoji support
Encrypted communication
Online/offline user status
Author
Tejashwini
Python Programming Internship Project
Oasis Infobyte
