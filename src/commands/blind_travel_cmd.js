var inp="$(query)"; 

var args = inp.split(" "); 

var x=args[6]; 
var z=args[8];

var dist=Math.sqrt(x*x+z*z);
var o;
if (dist < 190) {
    o = 190;
} else if (dist < 290) {
    o = dist;
} else if (dist < 442) {
    o = 290;
} else if (dist < 580) {
    o = 580;
} else if (dist < 692) {
    o = dist;
} else if (dist < 825) {
    o = 686;
} else if (dist < 970) {
    o = 970;
} else if (dist < 1060) {
    o = dist;
} else {
    o = 1060;
}

var t = Math.atan(z/x); 

var x_p = Math.sign(x)*Math.abs(o*Math.cos(t));
var z_p = Math.sign(z)*Math.abs(o*Math.sin(t));

x_p.toFixed(0) + ", " + z_p.toFixed(0)