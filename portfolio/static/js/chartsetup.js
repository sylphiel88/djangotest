var screenw = window.outerWidth / 1900;
var screenh = window.outerHeight / 1040;

document.getElementById("svg").setAttribute("width", Math.round(600 * screenw));
document.getElementById("svg").setAttribute("height", Math.round(400 * screenh));

document.getElementById("line100").setAttribute("x1", Math.round(20*screenw));
document.getElementById("line100").setAttribute("x2", Math.round(30*screenw));
document.getElementById("line100").setAttribute("y1", Math.round(80*screenh));
document.getElementById("line100").setAttribute("y2", Math.round(80*screenh));

document.getElementById("line75").setAttribute("x1", Math.round(20*screenw));
document.getElementById("line75").setAttribute("x2", Math.round(30*screenw));
document.getElementById("line75").setAttribute("y1", Math.round(155*screenh));
document.getElementById("line75").setAttribute("y2", Math.round(155*screenh));

document.getElementById("line50").setAttribute("x1", Math.round(20*screenw));
document.getElementById("line50").setAttribute("x2", Math.round(30*screenw));
document.getElementById("line50").setAttribute("y1", Math.round(230*screenh));
document.getElementById("line50").setAttribute("y2", Math.round(230*screenh));

document.getElementById("line25").setAttribute("x1", Math.round(20*screenw));
document.getElementById("line25").setAttribute("x2", Math.round(30*screenw));
document.getElementById("line25").setAttribute("y1", Math.round(305*screenh));
document.getElementById("line25").setAttribute("y2", Math.round(305*screenh));

document.getElementById("line0").setAttribute("x1", Math.round(20*screenw));
document.getElementById("line0").setAttribute("x2", Math.round(30*screenw));
document.getElementById("line0").setAttribute("y1", Math.round(380*screenh));
document.getElementById("line0").setAttribute("y2", Math.round(380*screenh));

var fonts = screenw>screenh?20*screenw:20*screenh;

document.getElementById("text100").setAttribute("x", Math.round(40*screenw));
document.getElementById("text100").setAttribute("y", Math.round(85*screenh));
document.getElementById("text100").setAttribute("style","font-size:"+Math.round(fonts)+"px");

document.getElementById("t0").setAttribute("x", Math.round(185*screenw));
document.getElementById("t0").setAttribute("y", Math.round(60*screenh));
document.getElementById("t0").setAttribute("style","font-size:"+Math.round(fonts)+"px");

document.getElementById("t1").setAttribute("x", Math.round(255*screenw));
document.getElementById("t1").setAttribute("y", Math.round(210*screenh));
document.getElementById("t1").setAttribute("style","font-size:"+Math.round(fonts)+"px");

document.getElementById("t2").setAttribute("x", Math.round(325*screenw));
document.getElementById("t2").setAttribute("y", Math.round(135*screenh));
document.getElementById("t2").setAttribute("style","font-size:"+Math.round(fonts)+"px");


document.getElementById("t3").setAttribute("x", Math.round(395*screenw));
document.getElementById("t3").setAttribute("y", Math.round(285*screenh));
document.getElementById("t3").setAttribute("style","font-size:"+Math.round(fonts)+"px");


document.getElementById("svgcontainer").style.width(Math.round((600*screenw))+"px");
document.getElementById("svgcontainer").style.height(Math.round((400*screenh))+"px");

var x1 = Math.round(170*screenw+70*0*screenw);
var x2 = Math.round(170*screenw+70*1*screenw);
var x3 = Math.round(170*screenw+70*2*screenw);
var x4 = Math.round(170*screenw+70*3*screenw);
var py1 = 1;
var py2 = 0.5;
var py3 = 0.75;
var py4 = 0.25;
var height1 = Math.round(300 * py1 * screenh);
var height2 = Math.round(300 * py2 * screenh);
var height3 = Math.round(300 * py3 * screenh);
var height4 = Math.round(300 * py4 * screenh);
var y1 = 380*screenh - height1;
var y2 = 380*screenh - height2;
var y3 = 380*screenh - height3;
var y4 = 380*screenh - height4;

document.getElementById("rect1").setAttribute("x", x1);
document.getElementById("rect1").setAttribute("y", y1);
document.getElementById("rect1").setAttribute("height", height1);
document.getElementById("rect1").setAttribute("width", Math.round(50*screenw));

document.getElementById("rect2").setAttribute("x", x2);
document.getElementById("rect2").setAttribute("y", y2);
document.getElementById("rect2").setAttribute("height", height2);
document.getElementById("rect2").setAttribute("width", Math.round(50*screenw));

document.getElementById("rect3").setAttribute("x", x3);
document.getElementById("rect3").setAttribute("y", y3);
document.getElementById("rect3").setAttribute("height", height3);
document.getElementById("rect3").setAttribute("width", Math.round(50*screenw));

document.getElementById("rect4").setAttribute("x", x4);
document.getElementById("rect4").setAttribute("y", y4);
document.getElementById("rect4").setAttribute("height", height4);
document.getElementById("rect4").setAttribute("width", Math.round(50*screenw));