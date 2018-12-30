//#############################################
// Connect SenseHat with virtual pins.
// One "listens" for reads events.
// Two sends SenseHat temperature.
// Four sends SenseHat GPS data.
//#############################################

var Blynk = require("blynk-library");
var sense = require("node-sense-hat");
var wia = require("wia");

var imu = sense.Imu;
var IMU = new imu.IMU();

// Workaround issue #7
//var blynk = new Blynk.Blynk(process.env.MY_BLYNK_TOKEN);
var blynk = new Blynk.Blynk(process.env.MY_BLYNK_TOKEN, options = {
  connector : new Blynk.TcpClient()
});

var wia = require('wia')(process.env.WIA_TOKEN_LOCATION);

//### virtual pin #one
var v1 = new blynk.VirtualPin(1);

//### virtual pin #two
var v2 = new blynk.VirtualPin(2);

//### virtual pin #three
var v3 = new blynk.VirtualPin(3);

//### virtual pin #four
var v4 = new blynk.VirtualPin(4);

var white = [255, 255, 255];
sense.Leds.clear();

// v1 write call back
v1.on('write', function(param) {
     var colour = param.map(Number);
     sense.Leds.clear(colour);
});

v2.on('read', function() {
  IMU.getValue(function (e, data) {
     v2.write(data.temperature);
  })
});

v3.on('write', function(param) {
  //check if it's too dark!
  if (param[0]<50){console.log("It's a bit dark")}
  if (param[0]>70){console.log("It's a bit bright")}
});

v4.on('write', function(param) {
 console.log("v4: lat. " + param[0])
 wia.locations.publish({
  latitude: param[0],
  longitude: param[1]
});
});

wia.stream.connect();
