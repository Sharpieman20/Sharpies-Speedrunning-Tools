var inp="$(query)"; 

var args = inp.split(" "); 

var x=args[6]; 
var z=args[8];

var dist=Math.sqrt(x*x+z*z);
var o;
if (dist < 190) {
    o = 190;
} else if (dist < 310) {
    o = dist;
} else if (dist < 460) {
    o = 310;
} else {
    o = 670;
}

var t = Math.atan(z/x); 

var x_p = Math.sign(x)*o*Math.cos(t); 
var z_p = Math.sign(z)*o*Math.sin(t); 

x_p.toFixed(0) + ", " + z_p.toFixed(0)