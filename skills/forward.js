const dgram = require('dgram')
const config = require('config').forward

exports.execute = (data) => {
  console.log(data)
  var keys = Object.keys(data)
  keys.forEach(function (key) {
    if (config.destinations[key]) {
      const client = dgram.createSocket('udp4')
      client.send(JSON.stringify(data[key]), config.destinations[key].port, config.destinations[key].address)
    }
  })
}
