$(document).ready(function(){
    var opr = 0;
    var num1 = 0;
    var num2 = 0;
    $("#btn1").click(function() {
        var val = $("#ausgabe").val();
        val +="1";
        $("#ausgabe").val(val);
        num1=opr==0?1:num1;
        num2=opr==1?1:num2;
    });
    $("#btn2").click(function() {
        var val = $("#ausgabe").val();
        val +="2";
        $("#ausgabe").val(val);
        num1=opr==0?1:num1;
        num2=opr==1?1:num2;
    });
    $("#btn3").click(function() {
        var val = $("#ausgabe").val();
        val +="3";
        $("#ausgabe").val(val);
        num1=opr==0?1:num1;
        num2=opr==1?1:num2;
    });
    $("#btn4").click(function() {
        var val = $("#ausgabe").val();
        val +="4";
        $("#ausgabe").val(val);
        num1=opr==0?1:num1;
        num2=opr==1?1:num2;
    });
    $("#btn5").click(function() {
        var val = $("#ausgabe").val();
        val +="5";
        $("#ausgabe").val(val);
        num1=opr==0?1:num1;
        num2=opr==1?1:num2;
    });
    $("#btn6").click(function() {
        var val = $("#ausgabe").val();
        val +="6";
        $("#ausgabe").val(val);
        num1=opr==0?1:num1;
        num2=opr==1?1:num2;
    });
    $("#btn7").click(function() {
        var val = $("#ausgabe").val();
        val +="7";
        $("#ausgabe").val(val);
        num1=opr==0?1:num1;
        num2=opr==1?1:num2;
    });
    $("#btn8").click(function() {
        var val = $("#ausgabe").val();
        val +="8";
        $("#ausgabe").val(val);
        num1=opr==0?1:num1;
        num2=opr==1?1:num2;
    });
    $("#btn9").click(function() {
        var val = $("#ausgabe").val();
        val +="9";
        $("#ausgabe").val(val);
        num1=opr==0?1:num1;
        num2=opr==1?1:num2;
    });
    $("#btn0").click(function() {
        var val = $("#ausgabe").val();
        val +="0";
        $("#ausgabe").val(val);
        num1=opr==0?1:num1;
        num2=opr==1?1:num2;
    });
    $("#btnplu").click(function() {
        if(opr==0) {
            var val = $("#ausgabe").val();
            val +="+";
            $("#ausgabe").val(val);
            opr=1;
        }
    });
    $("#btnmin").click(function() {
        if(opr==0) {
            var val = $("#ausgabe").val();
            val +="-";
            $("#ausgabe").val(val);
            opr=1;
        }
    });
    $("#btnmal").click(function() {
        if(opr==0) {    
            var val = $("#ausgabe").val();
            val +="*";
            $("#ausgabe").val(val);
            opr=1;
        }
    });
    $("#btndur").click(function() {
        if(opr==0) {    
            var val = $("#ausgabe").val();
            val +="/";
            $("#ausgabe").val(val);
            opr=1;
        }
    });
    $("#backs").click(function() {
        var val = $("#ausgabe").val();
        var char1 = val.substring(val.length-1, val.length);
        if(char1=="+" || char1=="-" || char1=="*" || char1=="/") {
            opr=0;
        } else if(val.substring(val.length-2,val.length-1)=="+" || val.substring(val.length-2,val.length-1)=="-" || val.substring(val.length-2,val.length-1)=="*" || val.substring(val.length-2,val.length-1)=="/") {
            num2=0;
        } else if(val.length==1) {
            num2=0;
        }
        val = val.substring(0,val.length-1);
        $("#ausgabe").val(val);
    });
    $("#btnret").click(function() {
        var numb1 = new Array();
        var n1=0;
        var n2=0;
        var numb2 = new Array();
        var oper = 0;
        var opt;
        if(num1!=0 && num2!=0 && opr!=0) {
            var val = $("#ausgabe").val();
            for(var i = 0; i<val.length;i++) {
                var char = val.substring(i,i+1);
                if(char=="+") {
                    oper=1
                    opt=1;
                }
                if(char=="-") {
                    oper=2
                    opt=1;
                }
                if(char=="*") {
                    oper=3
                    opt=1;
                }
                if(char=="/") {
                    oper=4
                    opt=1;
                }
                if(oper==0){
                    numb1[n1++]=parseInt(char);
                } else if(oper!=0 && opt==0) {
                    numb2[n2++]=parseInt(char);
                }
                opt=0;
            }
        }
        var ernum1 = 0;
        var len = numb1.length;
        for(var i=0;i<numb1.length;i++) {
            ernum1 += numb1[i]*(Math.pow(10,--len))
        }
        var ernum2 = 0;
        var len = numb2.length;
        for(var i=0;i<numb2.length;i++) {
            ernum2 += numb2[i]*(Math.pow(10,--len))
        }
        if(oper==1) {
            var ergebnis = ernum1+ernum2;
        }
        if(oper==2) {
            var ergebnis = ernum1-ernum2;
        }
        if(oper==3) {
            var ergebnis = ernum1*ernum2;
        }
        if(oper==4) {
            var ergebnis = ernum1/ernum2;
        }
        $("#ausgabe").val(ergebnis);
        opr=0;
        num1=1;
        num2=0;
    });
});