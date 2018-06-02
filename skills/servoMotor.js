const fs = require('fs');

const makePwmDriver = require('adafruit-i2c-pwm-driver');
const pwmDriver = makePwmDriver({address: 0x40, device: '/dev/i2c-1'});
pwmDriver.setPWMFreq(60);

var channels;
channels = JSON.parse(fs.readFileSync('./config.json', 'utf8'));

exports.execute = (data) => {
  console.log(data)
  var keys = Object.keys(data);
  for(var i = 0; i < keys.length; i++) {
    if(channels.hasOwnProperty(keys[i])){
      pwmDriver.setPWM(parseInt(channels[keys[i]]), 0, parseInt(data[keys[i]]));
    }
  }
}
