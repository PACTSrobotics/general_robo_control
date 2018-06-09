let skills = {
  servoMotor: require('./servoMotor')
}

exports.execute = (data) => {
  console.log(data)
  let keys = Object.keys(data)
  for (var i = 0; i < keys.length; i++) {
    skills[keys[i]].execute(data[keys[i]])
  }
}
