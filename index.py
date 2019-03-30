#!/usr/bin/python3
from skills.index import execute
import socket
import json
import yaml

cfg=yaml.load(open("./config.yml"))

# UDP_IP = "192.168.43.14"
UDP_IP = cfg["server"]["address"]
UDP_PORT = cfg["server"]["port"]

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = data.decode('utf-8').strip()
    jdata = json.loads(data)
    execute(jdata['commands'])
    print ("received message:", data)