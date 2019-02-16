#!/usr/bin/python3
from skills.servoMotor import execute
import socket
import json

UDP_IP = "192.168.43.14"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(data)
    data = data.decode('utf-8').strip()
    print(data)
    jdata = json.loads(data)
    execute(jdata['commands']['servoMotor'])
    print ("received message:", data)
