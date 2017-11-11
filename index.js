const PORT = 33333;
const HOST = '192.168.43.196';

const dgram = require('dgram');
const server = dgram.createSocket('udp4');
const fs = require('fs');

const makePwmDriver = require('adafruit-i2c-pwm-driver');
const pwmDriver = makePwmDriver({address: 0x40, device: '/dev/i2c-1'});
pwmDriver.setPWMFreq(60);

var chanels;

var sleep = require('sleep');

server.on('listening', function () {
    var address = server.address();
    console.log('UDP Server listening on ' + address.address + ":" + address.port);
    chanels = JSON.parse(fs.readFileSync('./config.json', 'utf8'));
});

server.on('message', function (message, remote) {
    var data = JSON.parse(message);
    if(data['robotSelect'] != undefined){
        chanels = JSON.parse(fs.readFileSync('./configs/'+ data['robotSelect'] +'.json', 'utf8'));
    }
    var keys = Object.keys(data);
    for(var i = 0; i < keys.length; i++) {
        if(chanels.hasOwnProperty(keys[i])){
            pwmDriver.setPWM(int(chanels[keys[i]]), 0, int(data[keys[i]]));
        }
    }
});

server.bind(PORT, HOST);

//sleep.sleep(1);
//pwmDriver.setPWM(0, 0, 150);
//sleep.sleep(2);
//pwmDriver.setPWM(0, 0, 600);
