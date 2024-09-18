import socket
import ipaddress
import threading
import time
import contextlib
import errno

maxPacketSize = 1024
defaultPort = 12345 # TODO: Change this to your expected port
serverIP = '127.0.0.1' #TODO: Change this to your instance IP

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
try:
    tcpPort = int(input("Please enter the TCP port of the host: "));
except:
    tcpPort = 0;
if tcpPort == 0:
    tcpPort = defaultPort;
tcpSocket.connect((serverIP, tcpPort));

clientMessage = "";
while clientMessage != "exit":
    clientMessage = input("Please type the message that you'd like to send (Or type \"exit\" to exit):\n>");

    # Send the message to your server
    tcpSocket.sendall(clientMessage.encode())

    if clientMessage == "query_best_highway":
        # Receive a reply from the server for the best highway to take
        serverResponse = tcpSocket.recv(maxPacketSize).decode()
        print(f"The best highway to take is: {serverResponse}")
    else:
        # If the message is not a query, just echo back the server's response
        echoResponse = tcpSocket.recv(maxPacketSize).decode()
        print(f"Server echoed: {echoResponse}")
    
tcpSocket.close();

