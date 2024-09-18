import socket
import ipaddress
import threading
import time
import contextlib
import errno
from dataclasses import dataclass
import random
import sys

maxPacketSize = 1024
defaultPort = 27017 #TODO: Set this to your preferred port
serverPort = input('Enter the socket for connection: \n')
serverIP = input('Enter the Ip address of the server: \n')

def GetFreePort(minPort: int = 1024, maxPort: int = 65535):
    for i in range(minPort, maxPort):
        print("Testing port",i);
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as potentialPort:
            try:
                potentialPort.bind((serverIP, i));
                potentialPort.close();
                print("Server listening on port",i);
                return i
            except socket.error as e:
                if e.errno == errno.EADDRINUSE:
                    print("Port",i,"already in use. Checking next...");
                else:
                    print("An exotic error occurred:",e);

def GetServerData() -> list[dict]:
    import MongoDBConnection as mongo
    return mongo.QueryDatabase()

# Method that passes in a list of traffic data (document objects) to return a dictionary 
# with key-value pairs of sensors and their list of traffic lengths
def sensor_data(traffic_data):
    # Initialize the dictionary
    sensorList = {}
    # Iterate through the collections in the traffic data.
    for data in traffic_data: 
        # Within the data, get the subfields under the field of 'payload'
        keys = data['payload'].keys()
        # Variable to store the sensor name from the payload.
        sensorName = ""
        # Iterate through the subfields of payload
        for key in keys:
            # If there is the string "Sensor" within any of the fields...
            if "Sensor" in key:
                # Store the name of that sensor
                sensorName = key
        # Get the traffic length of that sensor name.
        trafficLength = data['payload'][sensorName]
        # If that sensor name is already in the dictionary sensorList...
        if (sensorName in sensorList.keys()):
            # We append the list of traffic lengths for that particular sensor.
            sensorList[sensorName].append(trafficLength)
        # If that sensor name is not in the list...
        else:
            # It is the first sensor, so we add that sensor name to the dictionary, and give it the value of a 
            # list, where the first element of that list is the first traffic length of that particular sensor we got.
            sensorList[sensorName] = [trafficLength]
    # Return the dictionary of sensors and their list of traffic lengths.
    return sensorList


# Method that passes in a dictionary with key-value pairs of sensors and their list of traffic lengths 
# to return the sensor and its average traffic length, that is the minimum of traffic length all the sensors.
def calc_min_avg(sensorList):
    # Create a list of sensor values
    sensorValues = []
    # Iterate through sensor data dictionary, store sensor name and values
    for sensorName, values in sensorList.items():
        # Calculate the average of all the values for that sensor
        avg_traffic = sum(values) / len(values)
        # Append a tuple of the sensor name, and its average traffic to sensorValues list.
        sensorValues.append((sensorName, avg_traffic))

    #return lowest average traffic congestion from the list sensorValues 
    return min(sensorValues, key=lambda x: x[1])

running = True

def ListenOnTCP(connectionSocket, clientAddress):
    global running
    print("Connection from:", clientAddress)
    try:
        # Loop to run.
        while running:
            # Recieve message from client.
            clientMessage = connectionSocket.recv(maxPacketSize).decode()
            # If not message break from loop.
            if not clientMessage:
                break
            # Print the client message.
            print("Client message:", clientMessage)

            # Exit by typing exit.
            if clientMessage == "exit":
                print("Exiting Server")
                running = False
                break
            #For all client messa
            if clientMessage:
                # Invoke GetServerData to get data from the past five minutes.
                trafficData = GetServerData()

                # If there is traffic data
                if trafficData:
                    # Invoke sensor_data and pass in the traffic data to get a dictionary with devices and their corresponding
                    # traffic length
                    sensorData = sensor_data(trafficData)
                    # Invoke calc_min_avg and pass in the sensor data to get the minimum averages of the devices.
                    avg = calc_min_avg(sensorData)
                    # Send the average back to the client.
                    serverResponse = connectionSocket.send(bytearray(str(avg), encoding='utf-8'))
    finally:
        connectionSocket.close() # Close the connection
        print(f"Connection with {clientAddress} closed")

def CreateTCPSocket() -> socket.socket:
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    try:
        tcpPort = int(serverPort)  # This will find a free port dynamically
    except Exception as e:
        print("Failed to find a free port: ", e)
        sys.exit(1)  # Exit if no free port is available
    print("TCP Port:", tcpPort);
    tcpSocket.bind((serverIP, tcpPort));
    return tcpSocket;


def LaunchTCPThreads():
    tcpSocket = CreateTCPSocket();
    tcpSocket.listen(5);
    while True:
        connectionSocket, connectionAddress = tcpSocket.accept();
        connectionThread = threading.Thread(target=ListenOnTCP, args=[connectionSocket, connectionAddress]);
        connectionThread.start();


if __name__ == "__main__":
    tcpThread = threading.Thread(target=LaunchTCPThreads);
    tcpThread.start();

    try:
        while running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Server is shutting down.")
        running = False
        tcpThread.join()   # Wait for the network thread to finish

    print("Server has shut down successfully.")
