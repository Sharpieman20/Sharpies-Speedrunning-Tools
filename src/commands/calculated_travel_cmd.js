var inp="$(query)"; 

var args = inp.split(" "); 
var a=Math.abs;
var g=Math.sign;

var x=parseFloat(args[6]);
var z=parseFloat(args[8]);
var f=parseFloat(args[9]);
f%=360;
if (f < 0) {
    f += 360;
}
f -= 180;

var r=(90-f)*(Math.PI/180);

var m=-Math.tan(r);
var b=8-a(x%16)+16;
var l=[];
var s=0;

while (s<2688){
    var d=b*g(-f);
    x+=d;
    z+=d*m;
    var v=a(a(z%16)-8);
    s=Math.sqrt(x*x+z*z);
    if (s > 1408) {
        v*=2688/s;
        l.push({k:x,v:a(v),r:z});
    }
    b=16;
}

l.sort(function(u,i){return u.v-i.v;});
var h=l.shift();
(h.k/8).toFixed(0)+", "+(h.r/8).toFixed(0)