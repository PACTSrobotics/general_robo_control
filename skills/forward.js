const dgram = require('dgram')
const config = require('config').forward
const client = dgram.createSocket('udp4')

exports.execute = (data) => {
  console.log(data)
  var keys = Object.keys(data)
  keys.forEach(function (key) {
    if (config.destinations[key]) {
      client.socket.send(data[key], config.destinations[key].port, config.destinations[key].address)
    }
  })
}
