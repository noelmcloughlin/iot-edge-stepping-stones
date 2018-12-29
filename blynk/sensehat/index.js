//######################################
// Connect SenseHat with two virtual pins.
// One "listens" for reads events.
// Two returns SenseHat temperature.
//######################################
var Blynk = require("blynk-library");

var sense = require("node-sense-hat");
var imu = sense.Imu;
var IMU = new imu.IMU();

var AUTH = '"' + process.env.MY_BLYNK_TOKEN + '"';

var blynk = new Blynk.Blynk(AUTH);

//### virtual pin #one
var v1 = new blynk.VirtualPin(1);

//### virtual pin #two
var v2 = new blynk.VirtualPin(2);

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
