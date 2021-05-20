$('input[type=range]').on('input', function () {
    $(this).trigger('change');
});

$(document).ready(function(){
    calc(1);
    $("#zahl1").change(function(){
        calc(1);
    });
    $("#zahl2").change(function() {
        calc(2);
    });
    $("#zahl3").change(function() {
        calc(3);
    });
    $("#zahl4").change(function() {
        calc(4);
    });
});
function calc(chg) {
    var screenw = window.outerWidth / 1920;
    var screenh = window.outerHeight / 1040;
    var zahlen=new Array();
    var chgstr="#rect"+chg;
    $(chgstr).remove();
    for(i=0;i<4;i++) {
        var valstr="#zahl"+(i+1);
        zahlstr=$(valstr).val();
        zahlen[i]=zahlstr==""?0:parseInt(zahlstr);
    }
    var val=zahlen[chg-1];
    var max = Math.max.apply(Math, zahlen);
    for(i=0;i<4;i++) {
        var delstr = "#rect"+(i+1);
        $(delstr).remove();
        var val = zahlen[i];
        var x = Math.round(170*screenw+70*i*screenw);
        var py = val / max;
        var height = Math.round(300 * py * screenh);
        var y = 380*screenh - height;
        var svgns ="http://www.w3.org/2000/svg";
        var rect = document.createElementNS(svgns,"rect");
        var faktor = 127+Math.round(py*128);
        var fillstr=i==0?"rgb("+faktor+",0,0)":i==1?"rgb(0,0,"+faktor+")":i==2?"rgb(0,"+faktor+",0)":i==3?"rgb("+faktor+","+faktor+",0)":"";
        rect.setAttribute("id", "rect"+(i+1))
        rect.setAttribute("x", x);
        rect.setAttribute("y", y);
        rect.setAttribute("width", 50*screenw);
        rect.setAttribute("height", height);
        rect.setAttribute("style", "fill:"+fillstr)
        var fonts = screenw>screenh?20*screenw:20*screenh;
        document.getElementById("svg").appendChild(rect);
        document.getElementById("text100").innerHTML=max;
        document.getElementById("t"+i).setAttribute("y", y-20*screenh);
        document.getElementById("t"+i).setAttribute("x", x+10*screenw);
        document.getElementById("t"+i).setAttribute("fonts", "font-size:"+Math.round(fonts)+"px")
        document.getElementById("t"+i).innerHTML=zahlen[i];
    }
}