var inp="$(query)";

var args = inp.split(" ");

var p_f = parseFloat;
var f_a = (x, z) => degrees(atan2(z_i - z, x_i - x));
var f_s = (e, a) => min(sqrt(max((e-0.004)/(0.0001*((5-a)**3)),1)),16);
var f_f = (c) => c.toFixed(0);
var f_g = (d) => 16*round((d-8) / 16)+8;

var x_1 = p_f(args[0]);
var z_1 = p_f(args[1]);
var f_1 = p_f(args[2]);
var a_1 = p_f(args[3]);
var x_2 = p_f(args[4]);
var z_2 = p_f(args[5]);
var f_2 = p_f(args[6]);
var a_2 = p_f(args[7]);
var x_i = p_f(args[8]);
var z_i = p_f(args[9]);

var z_i, g_x, g_z;
var m_s = 2**33;

while (abs(x_i - x_1) <= 128+16) {

    z_i = ((x_i - x_1) * s_1) + z_1;
    x_i += 16;

    var g_s = (2**f_s(f_a(x_1, z_1) - f_1, a_1))*(2**f_s(f_a(x_2, z_2) - f_2, a_2));

    if (g_s < m_s) {
        m_s = g_s;
        g_x = x_i;
        g_z = f_g(z_i);
    }
}

f_f(g_x)+", "+f_f(g_z)