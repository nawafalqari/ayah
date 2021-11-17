const { exec } = require('child_process');

exec('python C:\\Users\\nawaf\\Desktop\\azkar_api\\examples\\get_zekr.py', function (err, stdout, stderr) {
  console.log(stdout);
  console.log(stdout)
  console.log(typeof stdout)
  var zkr = JSON.parse(stdout)
  console.log(zkr)
  console.log(typeof zkr)
});
