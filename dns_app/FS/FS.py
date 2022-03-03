import socket
import pickle
from flask import Flask 
from flask import request
import json


app = Flask(__name__)

def fibonacci(number):
    if number<=1:
        return 0
    elif number==1 or number==2:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)


@app.route('/fibonacci')
def fibonacci_request():
    args = request.args
    n = args['number']
    num= int(n)
    X=fibonacci(num)
    return X

def register1(as_ip, as_port, hostname, value, type, ttl):
    message = ((hostname, value, type, ttl))
    message_bytes = pickle.dumps(message)
    as_address = (as_ip, as_port)
    socket_con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_con.sendto(message_bytes, as_address)

@app.route('/register', methods=['PUT'])
def register2():
    data = request.json
    as_port  = data["as_port"]
    as_ip    = data["as_ip"]
    hostname = data["hostname"]
    fs_ip    = data["fs_ip"]
    ttl      = data["ttl"]
   
    register1(as_port=as_port,as_ip=as_ip,hostname=hostname,value=fs_ip,type="A",ttl=ttl)
    return "Registration is complete now"

app.run(host='0.0.0.0', port=9090,debug=True)