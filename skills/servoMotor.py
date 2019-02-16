
from adafruit_servokit import ServoKit
import yaml

cfg=yaml.load(open("./config.yml"))

pwmDriver = ServoKit(channels=16)

channels=cfg["servoMotor"]["motors"]

def execute(data):
	print(channels)
	print(data)
	for key in data:
		if key in channels:
			pwmDriver.setPWM(channels[key], 0, data[key])
