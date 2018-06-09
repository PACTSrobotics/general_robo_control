const PORT = 33333;
const HOST = '192.168.43.39';

const dgram = require('dgram');
const server = dgram.createSocket('udp4');
const skills = require('./skills')

server.on('listening', function () {
  var address = server.address();
  console.log('UDP Server listening on ' + address.address + ":" + address.port);
});

server.on('message', (message) => {
  var data = JSON.parse(message);
  skills.execute(data.commands)
})
server.bind(PORT, HOST);
