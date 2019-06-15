#!/usr/bin/python3
print('hi')
from skills.index import execute
import socket
import json
import yaml

cfg=yaml.load(open("./config.yml"))

# UDP_IP = "192.168.43.14"
UDP_IP = cfg["server"]["address"]
UDP_PORT = cfg["server"]["port"]
timeout = cfg["server"]["timeout"]

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
# sock.setblocking(0)
sock.settimeout(timeout)
print("listening on port", UDP_PORT)
while True:
    # with timeout(seconds=3):
    try:
        print("listening")
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        data = data.decode('utf-8').strip()
        jdata = json.loads(data)
        execute(jdata['commands'])
        print ("received message:", data)
    except socket.timeout as e:
        print(e)
        data={"servoMotor":{}}
        for drive in cfg["servoMotor"]["stop"]:
            val=cfg["servoMotor"]["stop"][drive]
            data["servoMotor"][drive]=val
        print(data)

        

