const config = require('config').server

const dgram = require('dgram');
const server = dgram.createSocket('udp4');
const skills = require('./skills')

server.on('listening', function () {
  var address = server.address();
  console.log('UDP Server listening on ' + address.address + ":" + address.port);
});

server.on('message', (message) => {
  try {
    var data = JSON.parse(message);
    skills.execute(data.commands)
  } catch (e) {
    console.log(e)
  }
})
server.bind(config.port, config.address);
