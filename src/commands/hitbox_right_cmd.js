var inp="$(query)";

var args = inp.split(" ");

var x = args[6];
var z = args[8];
var f = parseFloat(args[9]);

var error=f%90.0;
error -= 45.0;
error *= 0.0111;
error *= error;
error = 0.845 - error;

f+error