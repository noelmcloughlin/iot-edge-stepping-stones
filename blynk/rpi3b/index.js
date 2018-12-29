//###########################################
// Blynk provides iOS and Android apps to
// control devices over TCP/IP or Bluetooth.
//
// This script creates a virtual pin V1
// to communicate with your BlynkApp.
//###########################################

var BlynkLib = require('blynk-library');
var blynk = new BlynkLib.Blynk(process.env.MY_BLYNK_TOKEN);

var v1 = new blynk.VirtualPin(1);
v1.on('write', function(param) {
  console.log('V1:', param);
});
