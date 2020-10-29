var inp="$(query)";

var args = inp.split(" ");

var x=args[6];
var z=args[8];
var f=args[9];
f+=180;
f%=360;
if (f < -180) {
    f += 360;
}

var o=256;
var d = 90-f;

var x_1 = x/8;
var z_1 = z/8;
var r = d * (Math.PI/180);

var m_1 = -1 * Math.tan(r);
var a = 1 + (m_1*m_1);
var b_1 = -1*m_1*x_1 + z_1;
var b = 2 * m_1 * b_1;
var c_o = b_1*b_1 - o*o;

var x_p = ((-1*b) - (Math.sign(f)*Math.sqrt(b*b - 4*a*c_o)))/(2*a);
var z_p = m_1*x_p + b_1;

x_p.toFixed(0) + ", "+ z_p.toFixed(0)