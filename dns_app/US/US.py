import socket
import pickle
from flask import Flask 
from flask import request
import json



app = Flask(__name__)

def function(hostname, as_ip, as_port):
    as_address = (as_ip, int(as_port))
    socket_con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = None
    message_bytes = pickle.dumps(("A", hostname))
    as_ip = None
    response = pickle.loads(socket_con.sendto(msg_bytes, (as_ip, int(as_port)))
    ttl = response
    return fs_ip


@app.route('/fibonacci', methods=["GET"])
def fibonacci():
    as_port  = request.args.get('as_port'))
    as_ip    = request.args.get('as_ip')
    hostname = request.args.get('hostname')
    fs_port  = request.args.get('fs_port'))
    fs_ip = function(hostname=hostname,as_ip=as_ip,as_port=as_port)
    number   = request.args.get('number'))
    return requests.get(f"http://{}:{}/fibonacci?number={}'.format(fs_port,number)


app.run(host='0.0.0.0',port=8080,debug=True)