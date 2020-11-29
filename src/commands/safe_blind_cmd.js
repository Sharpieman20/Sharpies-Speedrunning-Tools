var inp="$(query)"; 

var args = inp.split(" "); 

var x=args[6]; 
var z=args[8];

var dist=Math.sqrt(x*x+z*z);
var o;
if (dist < 222) {
    o = 222;
} else if (dist < 250) {
    o = dist;
} else if (dist < 480) {
    o = 250;
} else if (dist < 615) {
    o = 615;
} else if (dist < 645) {
    o = dist;
} else if (dist < 832) {
    o = 645;
} else if (dist < 1005) {
    o = 1005;
} else if (dist < 1032) {
    o = dist;
} else {
    o = 1032;
}

var t = Math.atan(z/x); 

var x_p = Math.sign(x)*Math.abs(o*Math.cos(t));
var z_p = Math.sign(z)*Math.abs(o*Math.sin(t));

x_p.toFixed(0) + ", " + z_p.toFixed(0)