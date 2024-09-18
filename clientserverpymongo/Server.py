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
defaultPort = 5123 #TODO: Set this to your preferred port

def GetFreePort(minPort: int = 1024, maxPort: int = 65535):
    for i in range(minPort, maxPort):
        print("Testing port",i);
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as potentialPort:
            try:
                potentialPort.bind(('localhost', i));
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

def sensor_data(traffic_data):
    # Dictionary to hold lists of traffic values for each sensor
    sensors_data = {
        'Traffic Sensor on 110 Freeway': [],
        'Traffic Sensor #2 on the 110 Freeway': [],
        'Traffic Sensor #3 on the 110 Freeway': []
    }

    # Populate the dictionary with traffic values
    for data in traffic_data:
        for sensor_name in sensors_data.keys():
            if sensor_name in data['payload']:
                sensors_data[sensor_name].append(int(data['payload'][sensor_name]['$numberInt']))

    # Convert dictionary to a list of lists containing sensor name and traffic values
    sensor_values_list = [[sensor] + values for sensor, values in sensors_data.items()]
    return sensor_values_list

def calculate_avg_find_best(sensor_values_list):
    averages = []
    for sensor_data in sensor_values_list:
        sensor_name = sensor_data[0]
        values = sensor_data[1:]
        if values:
            average_traffic = sum(values) / len(values)
            averages.append((sensor_name, average_traffic))
        else:
            averages.append((sensor_name, float('inf')))  # Use 'inf' if no data to avoid division by zero

    # Find the sensor with the lowest average traffic value
    best_sensor, best_average = min(averages, key=lambda x: x[1])
    return best_sensor, best_average

running = True

def ListenOnTCP(connectionSocket, clientAddress):
    global running
    print("Connection from:", clientAddress)
    try:
        while running:
            client_message = connectionSocket.recv(maxPacketSize).decode()
            if not client_message:
                break
            print("Client message:", client_message)

            if client_message == "query_best_highway":
                traffic_data = GetServerData()
                if traffic_data:
                    sensor_values_list = sensor_data(traffic_data)
                    best_sensor, best_average = calculate_avg_find_best(sensor_values_list)
                    response = f"The best route is on {best_sensor} with an AverageOnFreeway of {best_average:.2f}"
                else:
                    response = "No traffic data available to calculate the best highway."
            elif client_message == "exit":
                response = "Server shutting down."
                running = False
            else:
                response = client_message.upper()  # Echo back the uppercase version of the client's message

            connectionSocket.sendall(response.encode())

    finally:
        connectionSocket.close()
        print(f"Connection with {clientAddress} closed")

def CreateTCPSocket() -> socket.socket:
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    tcpPort = defaultPort
    print("TCP Port:",tcpPort);
    tcpSocket.bind(('localhost', tcpPort));
    return tcpSocket;

def LaunchTCPThreads():
    tcpSocket = CreateTCPSocket();
    tcpSocket.listen(5);
    while True:
        connectionSocket, connectionAddress = tcpSocket.accept();
        connectionThread = threading.Thread(target=ListenOnTCP, args=[connectionSocket, connectionAddress]);
        connectionThread.start();


if __name__ == "__main__":
    tcpSocket = CreateTCPSocket()
    tcpThread = threading.Thread(target=LaunchTCPThreads);
    tcpThread.start();

    try:
        while running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Server is shutting down.")
        running = False
