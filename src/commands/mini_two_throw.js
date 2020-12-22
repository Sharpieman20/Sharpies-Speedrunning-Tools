var n="$(query)";

var r = n.split(" ");

var p = parseFloat;
var f_a = (x, z) => (((180/Math.PI)*Math.atan2(z_i - z, x_i - x)))-90;
var f_s = (e, a) => min(Math.sqrt(max((e-0.004)/(0.0001*((5-a)**3)),1)),16);
var f_f = (c) => c.toFixed(0);

var x_1, z_1, x_2, z_2, x_i, z_i = [0, 1, 4, 8, 9].map(q => p(r[q]));

var z_i, g_x, g_z;
var m_s = 2**33;

for (i=0;i<10;i++) {

    z_i = ((x_i - x_1) * s_1) + z_1;
    x_i += 16;

    var g_s = (2**f_s(f_a(x_1, z_1) - p(r[2]), p(r[3])))*(2**f_s(f_a(x_2, z_2) - p(r[6]), p(r[7])));

    if (g_s < m_s) {
        m_s = g_s;
        g_x = x_i;
        g_z = 16*Math.round((d-8) / 16)+8;
    }
}

f_f(g_x)+", "+f_f(g_z)