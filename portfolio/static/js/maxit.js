var pressed;
var currply = 1;
var ply1scr = 0;
var ply2scr = 0;
document.addEventListener('keydown', logKey);
currx = Math.floor(Math.random() * 8)
curry = Math.floor(Math.random() * 8)
stdzahlen = [-9,-7,-6,-6,-5,-5,-4,-4,-4,-3,-3,-3,-2,-2,-2,-2,-1,-1,-1,-1,-1,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,7,7,7,8,8,9,9,10,15];
stdzahlen = shuffle(stdzahlen);
zahlenarray = Array(8);
for(i=0;i<8;i++) {
    zahlenarray[i]=Array(8);
}
empty = 0;
for(i=0;i<8;i++) {
    for(j=0;j<8;j++) {
        if(i==currx&&j==curry) {
            empty=1;
            zahlenarray[i][j]=20;
        } else {
            zahlenarray[i][j] = stdzahlen[8*+i+j-empty];
        }
    }
}
console.log(zahlenarray);
rebuild(true);

function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;
    while (0 !== currentIndex) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }
    return array;
}

function logKey(e){
    pressed=e.code;
    if(pressed=="KeyW" && currply==2) {
        delold();
        notfound=0;
        anzleere=0;
        while(notfound==0 && anzleere != 8) {
            curry==0?curry=7:curry-=1;
            if(zahlenarray[currx][curry]==20) {
                anzleere+=1;
            } else {notfound=1;}
        }
        rebuild(false);
    } else
    if(pressed=="KeyS" && currply==2) {
        delold();
        notfound=0;
        anzleere=0;
        while(notfound==0 && anzleere != 8) {
            curry==7?curry=0:curry+=1;
            if(zahlenarray[currx][curry]==20) {
                anzleere+=1;
            } else {notfound=1;}
        }
        rebuild(false);
    } else
    if(pressed=="KeyA" && currply==1) {
        delold();
        notfound=0;
        anzleere=0;
        while(notfound==0 && anzleere != 8) {
            currx==0?currx=7:currx-=1;
            if(zahlenarray[currx][curry]==20) {
                anzleere+=1;
            } else {notfound=1;}
        }
        rebuild(false);
    } else
    if(pressed=="KeyD" && currply==1) {
        delold();
        notfound=0;
        anzleere=0;
        while(notfound==0 && anzleere != 8) {
            currx==7?currx=0:currx+=1;
            if(zahlenarray[currx][curry]==20) {
                anzleere+=1;
            } else {notfound=1;}
        }
        rebuild(false);
    } else
    if(pressed=="Enter") {
        if(zahlenarray[currx][curry]!=20) {
            currply==1?currply=2:currply=1;
            ply1scr+=currply==1?parseInt(document.getElementById("Text"+currx+curry).innerHTML):0;
            ply2scr+=currply==2?parseInt(document.getElementById("Text"+currx+curry).innerHTML):0;
            zahlenarray[currx][curry]=20;
            document.getElementById("Text"+currx+curry).innerHTML="";
            document.getElementById("player1").innerHTML=ply1scr;
            document.getElementById("player2").innerHTML=ply2scr;
            document.getElementById("currply").innerHTML="Spieler "+currply+" ist dran!"
            rebuild(false);
        }
        anzahleerex=0;
        anzahleerey=0;
        for(i=0;i<8;i++) {
            anzahleerex+=zahlenarray[i][curry]==20?1:0;
            anzahleerey+=zahlenarray[currx][i]==20?1:0;
        }
        if((anzahleerex==8 && currply==1)||(anzahleerey==8&&currply==2)) {
            finishgame();
        }
    }
}

function rebuild(neworold) {
    for(i=0;i<8;i++) {
        for(j=0;j<8;j++) {
            if(neworold) {
                var svgns ="http://www.w3.org/2000/svg";
                var rect = document.createElementNS(svgns,"rect");
                rect.setAttribute("id", "Feld"+i+j);
                rect.setAttribute("width", 50);
                rect.setAttribute("height", 50);
                rect.setAttribute("x", i*50);
                rect.setAttribute("y", 20+j*50);
                if(i==currx&&j!=curry) {      
                    rect.setAttribute("style", "fill:rgba(255,0,0,0.2); stroke-width:1px; stroke:red");
                } else if(i!=currx&&j==curry) {      
                    rect.setAttribute("style", "fill:rgba(0,0,255,0.2); stroke-width:1px; stroke:blue");
                } else if(i==currx&&j==curry && currply==1) {      
                    rect.setAttribute("style", "fill:rgba(0,0,255,0.5); stroke-width:1px; stroke:blue");
                } else if(i==currx&&j==curry && currply==2) {
                    rect.setAttribute("style", "fill:rgba(255,0,0,0.5); stroke-width:1px; stroke:blue");
                } else {
                    rect.setAttribute("style", "fill:rgba(255,255,255,0.2); stroke-width:1px; stroke:black");
                }
                document.getElementById("svgmaxit").appendChild(rect);
                if(zahlenarray[i][j]!=20) {
                    var text = document.createElementNS(svgns, "text");
                    text.setAttribute("id", "Text"+i+j);
                    text.setAttribute("x",i*50+20);
                    text.setAttribute("y",j*50+50);
                    text.innerHTML=zahlenarray[i][j];
                    document.getElementById("svgmaxit").appendChild(text);
                } else {
                    var text = document.createElementNS(svgns, "text");
                    text.setAttribute("id", "Text"+i+j);
                    text.setAttribute("x",i*50+20);
                    text.setAttribute("y",j*50+50);
                    document.getElementById("svgmaxit").appendChild(text);
                }
            } else {
                var rect = document.getElementById("Feld"+i+j);
                if(i==currx&&j!=curry) {      
                    rect.setAttribute("style", "fill:rgba(255,0,0,0.2); stroke-width:1px; stroke:red");
                } else if(i!=currx&&j==curry) {      
                    rect.setAttribute("style", "fill:rgba(0,0,255,0.2); stroke-width:1px; stroke:blue");
                } else if(i==currx&&j==curry && currply==1) {      
                    rect.setAttribute("style", "fill:rgba(0,0,255,0.5); stroke-width:1px; stroke:blue");
                } else if(i==currx&&j==curry && currply==2) {
                    rect.setAttribute("style", "fill:rgba(255,0,0,0.5); stroke-width:1px; stroke:blue");
                } else {
                    rect.setAttribute("style", "fill:rgba(255,255,255,0.2); stroke-width:1px; stroke:black");
                }
            }
        }
    }
}

function delold() {
    for(i=0;i<8;i++) {
        for(j=0;j<8;j++) {
            var rect = document.getElementById("Feld"+i+j);
            rect.setAttribute("style", "fill:rgba(255,255,255,0); stroke-width:1px; stroke:black");
        }
    }
}

function finishgame() {
    console.log("hier!");
    var svgns ="http://www.w3.org/2000/svg";
    var text = document.createElementNS(svgns,"text");
    text.setAttribute("x","500");
    text.setAttribute("y","380");
    if(ply1scr>ply2scr){
        text.innerHTML="Spieler 1 hat gewonnen!!!";
    } else if(ply1scr==ply2scr){
        text.innerHTML="Unentschieden!!!";
    } else {
        text.innerHTML="Spieler 2 hat gewonnen!!!";
    }
    document.getElementById("svgmaxit").appendChild(text);
}