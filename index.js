const PORT = 33333;
const HOST = '192.168.240.210';

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
server.bind(PORT, HOST);
