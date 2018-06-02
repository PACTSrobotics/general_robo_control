let skills = {
  servoMotor: require('./servoMotor')
}

module.exports.execute => (data) {
  let keys = Object.keys(data.commands)
  for (var i = 0; i < keys.length; i++) {
    skills[keys[i]].execute(data.commands[keys[i]])
  }
}
