from adafruit_servokit import ServoKit
import yaml
from playsound import playsound

cfg=yaml.load(open("./config.yml"))

pwmDriver = ServoKit(channels=16)

motors=cfg["servoMotor"]["motors"]

def execute(data):
	for key in data:
		if key =="servoMotor":
			executeServoMotor(data["servoMotor"])
		if key == "playsound":
			executeSound()

def executeServoMotor(data):
	for key in data:
		if key in motors:
			# print (data[key])
			pwmDriver.servo[motors[key]].angle = data[key]
	
def executeSound():
	playsound(cfg["sound"]["fileName"])






# {"commands":{"servoMotor":{"leftDrive":600}, "playsound":1}}
# {"commands":{"servoMotor":{"leftDrive":600}}}