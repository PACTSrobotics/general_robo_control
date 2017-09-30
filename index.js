const PORT = 33333;
const HOST = '192.168.43.196';

const dgram = require('dgram');
const server = dgram.createSocket('udp4');

const makePwmDriver = require('adafruit-i2c-pwm-driver');
const pwmDriver = makePwmDriver({address: 0x40, device: '/dev/i2c-1'});
pwmDriver.setPWMFreq(60);

const chanels = {
    head : "0",
    left_leg : "1",
    right_leg: "2"
}

var sleep = require('sleep');

server.on('listening', function () {
    var address = server.address();
    console.log('UDP Server listening on ' + address.address + ":" + address.port);
});

server.on('message', function (message, remote) {
    console.log(remote.address + ':' + remote.port +' - ' + message);
    var data = JSON.parse(message);
    console.log(data);
    var keys = Object.keys(data);
    for(var i = 0; i < keys.length; i++) {
        if(chanels.hasOwnProperty(keys[i])){
            pwmDriver.setPWM(chanels[keys[i]], 0, data[keys[i]]);
            console.log(keys[i]);
            console.log(chanels[keys[i]]);
            console.log(data[keys[i]]);
        }
    }
});

server.bind(PORT, HOST);

//sleep.sleep(1);
//pwmDriver.setPWM(0, 0, 150);
//sleep.sleep(2);
//pwmDriver.setPWM(0, 0, 600);
