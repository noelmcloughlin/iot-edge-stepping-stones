//###########################################
// Creates Blynk "Virtual Pin" for a device,
// used to interface, display, and send data
// to/from BlynkApp on Android/iOS.
//###########################################

var Blynk = require("blynk-library");
var AUTH = process.env.MY_BLYNK_TOKEN;

var blynk = new Blynk.Blynk(AUTH);
var v1 = new blynk.VirtualPin(1);

v1.on('write', function(param) {
  console.log('V1:', param[0]);
});
