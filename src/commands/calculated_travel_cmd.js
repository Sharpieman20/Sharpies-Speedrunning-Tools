var inp="$(query)"; 

var args = inp.split(" "); 

var x=parseFloat(args[6]); 
var z=parseFloat(args[8]);
var f=parseFloat(args[9]);

var g=Math.sign;
var a=Math.abs;

var r=(90-f)*(Math.PI/180);

var c=Math.cos(r);
var w=g(x)*c;
var m=g(z)*Math.sin(r);
var b=16-(x%16)+8;
var l=[];

while (a(x)<9000){
    var d=b/c;
    x+=d*w;
    z+=d*m;
    l.push({k:x,v:a(a(z%16)-8),r:z});
    b=16;}

l.sort(function(u,i){return u.v-i.v;});

var h=l.shift();
h.k+", "+h.r