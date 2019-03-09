from adafruit_servokit import ServoKit
import yaml
#from playsound import playsound
import subprocess
import socket


cfg=yaml.load(open("./config.yml"))

pwmDriver = ServoKit(channels=16)

motors=cfg["servoMotor"]["motors"]
parts=cfg["forward"]

def execute(data):
	for key in data:
		if key =="servoMotor":
			executeServoMotor(data["servoMotor"])
		if key == "playsound":
			executeSound()
		if key == "lights":
			executeLights(data["lights"])
		if key == "forward":
			forwarder(data["forward"])


def executeServoMotor(data):
	for key in data:
		if key in motors:
			# print (data[key])
			pwmDriver.servo[motors[key]].angle = data[key]
	
def executeSound():
	subprocess.Popen(["omxplayer",cfg["sound"]["fileName"]])

def forwarder(data):
	for key in data:
		if key in parts:
			UDP_IP = cfg["forward"][key]["address"]
			UDP_PORT = cfg["forward"][key]["port"]
			sock = socket.socket(socket.AF_INET, # Internet
				socket.SOCK_DGRAM) # UDP
			message=bytearray(data[key], "utf-8")
			sock.sendto(message, (UDP_IP, UDP_PORT))
			

def executeLights(data):
	pin = cfg["lights"]["pin"]
	if data==0:
		#set pin to off
		pass
	elif data == 1:
		#set pin to on
		pass
	





# {"commands":{"servoMotor":{"leftDrive":90}, "playsound":1}}
# {"commands":{"servoMotor":{"leftDrive":90}}}
# {	"servoMotor":{"leftDrive":90}, 
# 	"playsound":1,
# 	"forward":{'head':{"commands":{"lights":1, 'servoMotor':{"mainDrive":90}}}}
# }
# {"commands":{"forward":{"head":{"commands":{"sevoMotor":{"mainDrive":90}}}}, "playsound":1}}