import json
import Adafruit_PCA9685
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

pwm = Adafruit_PCA9685.PCA9685()
port = 33333
pwm.set_pwm_freq(60)

with open('./config.json', 'r') as configFile:
    channels = json.loads(configFile.read())

class Echo(DatagramProtocol):

    def datagramReceived(self, data, (host, port)):
        inputData = json.loads(data)
        for key in inputData:
            if(channels.get(key, None) != None):
                pwm.set_pwm(int(channels.get(key)), 0, int(inputData.get(key)))
        print "receieved %r from %s:%d" % (data, host, port)

reactor.listenUDP(port, Echo())
reactor.run()
