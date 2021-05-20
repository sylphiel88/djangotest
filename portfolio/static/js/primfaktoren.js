$(document).ready(function() {
    $("#zahl").keyup(function() {
        var zahl = $("#zahl").val();
        console.log("Hallo");
        var regi = /^[0-9]*$/;
        var booli = regi.test(zahl);
        $(".ppfz").remove();
        if(booli) {
            $("#pfz").append("<p class=\"teal-text ppfz\"><b>Ergebnis: " + pfz(zahl) + "</b></p>");
        } else{
            $("#pfz").append("<p class=\"teal-text ppfz\">Bitte Zahl eingeben!</p>");
        }
    });
});

function pfz(zahl) {
    var j = 0;
    var faktoren = new Array();
    var multipliers = new Array();
    var temp = zahl;
    console.log(zahl);
    for(var i=2; i<= temp;i++) {
        if(temp%i==0) {
            if(faktoren[j-1]!=i) {
                faktoren[j]=i;
                multipliers[j]=1;
                j++;
            } else {
                multipliers[j-1]+=1;
            }
            temp = temp / i;
            i=1;
        }
    }
    var retstri = "";
    if(prim(zahl)) {
        retstri = zahl;
    } else {
        for(i=0;i<faktoren.length;i++) {
            if(i!=faktoren.length-1) {
                if(multipliers[i]>1) {
                    retstri += faktoren[i] + "<sup>" + multipliers[i] +"</sup>" + "*";
                } else {
                    retstri += faktoren[i] +"*";
                }
            } else {
                if(multipliers[i]>1) {
                    retstri += faktoren[i] + "<sup>" + multipliers[i] +"</sup>";
                } else {
                    retstri += faktoren[i];
                }
            }
        }
    }
    return retstri;
}

function prim(zahl) {
    for(var i = 2; i < zahl; i++)
      if(zahl % i === 0) return false;
    return zahl > 1;
  }

function teilbar(zahl, teiler) {
    return zahl%teiler==0;
}