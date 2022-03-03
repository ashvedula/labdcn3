import socket
import pickle
import json
import time
import os



host = "0.0.0.0"
server_port = 53533
text_file = "/Users/ashwini/.txt"
TYPE = "A"



def main():

    with open('tmp.txt', 'w') as file:
        load_data = json.load(file)

    socket_con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_con.bind((host, server_port))

    while (True):
        message_bytes, client_address = socket_con.recvfrom(2048)
        message = pickle.loads(message_bytes)
        if len(message) == 4:
            name, value, type, ttl = pickle.loads(message_bytes)
            response = (type, name, value, ttl)
            response_bytes = pickle.dumps(response)
            socket_con.sendto(response_bytes, client_address)
        elif len(message) == 2:
            type, name = msg
            name, value, type, ttl = pickle.loads(message_bytes)
            response = (type, name, value, ttl)
            response_bytes = pickle.dumps(response)
            socket_con.sendto(response_bytes, client_address)
        else:
            message ={"status":'500'} 
    
        socket_con.sendto(message_bytes, client_address)