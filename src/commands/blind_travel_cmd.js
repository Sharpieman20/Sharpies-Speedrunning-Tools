var inp=$(query);

var ideal=216;
var f = 90-inp;

var r = f * (Math.PI/180);

var x = -1*Math.cos(r)*ideal;
var z = Math.sin(r)*ideal;

var xFormatted = x.toFixed(2);
var zFormatted = z.toFixed(2);

xFormatted + ", " + zFormatted