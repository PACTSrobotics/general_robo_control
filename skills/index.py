from adafruit_servokit import ServoKit
import yaml
#from playsound import playsound
import subprocess
import socket
import json
import board
import busio
import digitalio
import adafruit_mcp230xx

cfg=yaml.load(open("./config.yml"))


motors=cfg["servoMotor"]["motors"]
parts=cfg["forward"]
pins = cfg["digitalIO"]["pins"]

if cfg["servoMotor"]["enable"]:

	pwmDriver = ServoKit(channels=16)

if cfg["digitalIO"]["enable"]:

	i2c = busio.I2C(board.SCL, board.SDA)
	mcp = adafruit_mcp230xx.MCP23017(i2c)  # MCP23017

	for i in range(16):
		mcp.get_pin(i).switch_to_output(value=True)


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
		if key == "digitalIO":
			executeDigitalIO(data["digitalIO"])


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
			message=bytearray(json.dumps(data[key]), "utf-8")
			sock.sendto(message, (UDP_IP, UDP_PORT))


def executeLights(data):
	pin = cfg["lights"]["pin"]
	if data==0:
		#set pin to off
		pass
	elif data == 1:
		#set pin to on
		pass

def executeDigitalIO(data):
	for key in data:
		if key in pins:
			mcp.get_pin(pins[key]).value = data[key]




# {"commands":{"servoMotor":{"leftDrive":90}, "playsound":1}}
# {"commands":{"servoMotor":{"leftDrive":90}}}



# {	"servoMotor":{"leftDrive":90},
# 	"playsound":1,
# 	"forward":{'head':{"commands":{"lights":1, 'servoMotor':{"mainDrive":90}}}}
# }

#{"commands":{"digitalIO":{"led0":1}}}

# {"commands":{"forward":{"head":{"commands":{"sevoMotor":{"mainDrive":90}}}}, "playsound":1}}

#{"commands":{"forward":{"head":{"commands":{"servoMotor":{"mainDrive":90}}}}}}
#{"commands":{"forward":{"head":{"commands":{"servoMotor":{"mainDrive":95}}}}}}

