//###########################################
// Create Blynk "Virtual Pin" for a device,
//###########################################

var Blynk = require("blynk-library");

// Workaround issue #7
//var blynk = new Blynk.Blynk(process.env.MY_BLYNK_TOKEN);
var blynk = new Blynk.Blynk(process.env.MY_BLYNK_TOKEN, options = {
  connector : new Blynk.TcpClient()
});

var v1 = new blynk.VirtualPin(1);
v1.on('write', function(param) {
  console.log('V1:', param[0]);
});
