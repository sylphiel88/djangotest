document.addEventListener('keydown', pressedKey);
var i,j;
canvas = document.getElementById("canvas");
ccontext = canvas.getContext("2d");
class Rectangle {
    constructor(x,y) {
        this.x=x;
        this.y=y;
        this.h=20;
        this.w=20;
    }
}

var firstMove=false;

class Snake {
    constructor() {
        this.tiles=[[5,5],[6,5],[7,5],[8,5],[9,5]];
        this.d = "w";
    }
}

fields = [];
for(i=0;i<20;i++) {
    tempfield=[];
    for(j=0;j<20;j++) {
        if(i==0||j==0||i==19||j==19){
            ccontext.beginPath();
            tempfield.push(new Rectangle(i*20,j*20));
            ccontext.fillStyle='#808080';
            ccontext.fillRect(i*20,j*20,20,20);
            ccontext.stroke();
        } else {
            ccontext.beginPath();
            tempfield.push(new Rectangle(i*20,j*20));
            ccontext.rect(i*20,j*20,20,20);
            ccontext.stroke();
        }
    }
    fields.push(tempfield);
}
class Fruit {
    constructor() {
        var x = Math.floor(Math.random()*18+1);
        var y = Math.floor(Math.random()*18+1);
        theSnake.tiles.forEach(field => {
            var xf = field[0];
            var yf = field[1];
            if(x==xf&&y==yf) {
                x = Math.floor(Math.random()*18+1);
                y = Math.floor(Math.random()*18+1);
            }
        });
        console.log(x,y);
        this.x=x;
        this.y=y;
        ccontext.beginPath();
        ccontext.fillStyle='#9CF740';
        ccontext.fillRect(20*x,20*y,20,20);
        ccontext.stroke();
    }
    delFruit() {
        x = this.x;
        y = this.y;
        ccontext.beginPath();
        ccontext.fillStyle='#FFFFFF';
        ccontext.fillRect(x*20,y*20,20,20);
        ccontext.rect(x*20,y*20,20,20)
        ccontext.stroke();
    }
}
theSnake = new Snake();
theFruit = new Fruit();

function drawSnake(){
    var i = 0;
    theSnake.tiles.forEach(field => {
        x=fields[field[0]][field[1]].x;
        y=fields[field[0]][field[1]].y;
        ccontext.beginPath();
        ccontext.fillStyle = (i==0?'#990000':(i==theSnake.tiles.length-1?'#500000':'#FF0000'));
        ccontext.fillRect(x,y,20,20);
        ccontext.stroke();
        i++;
    });
}
function moveSnake() {
    d=theSnake.d;
    xh=theSnake.tiles[0][0];
    yh=theSnake.tiles[0][1];
    xh1=fields[xh][yh].x;
    yh1=fields[xh][yh].y;
    xt=theSnake.tiles[theSnake.tiles.length-1][0];
    yt=theSnake.tiles[theSnake.tiles.length-1][1];
    xt1=fields[xt][yt].x;
    yt1=fields[xt][yt].y;
    ccontext.beginPath();
    ccontext.fillStyle = '#FF0000';
    ccontext.fillRect(xh1,yh1,20,20);
    ccontext.stroke();
    ccontext.beginPath();
    ccontext.fillStyle='#FFFFFF';
    ccontext.fillRect(xt1,yt1,20,20);
    ccontext.rect(xt1,yt1,20,20);
    ccontext.stroke();
    head = theSnake.tiles[0];
    if(d=="w"){
        newField=[head[0]-1,head[1]];
    } else if(d=="e") {
        newField=[head[0]+1,head[1]];
    } else if(d=="n") {
        newField=[head[0],head[1]-1];
    } else {
        newField=[theSnake.tiles[0][0],theSnake.tiles[0][1]+1];
    }
    theSnake.tiles = [newField].concat(theSnake.tiles);
    if(xh==theFruit.x&&yh==theFruit.y){
        console.log('geht');
        theFruit = new Fruit();
    } else {
        theSnake.tiles.pop(theSnake.tiles.length-1);
    }
    xh=theSnake.tiles[0][0];
    yh=theSnake.tiles[0][1];
    xh1=fields[xh][yh].x;
    yh1=fields[xh][yh].y;
    if(xh==0||xh==19||yh==0||yh==19) {
        endGame();
        return null;
    }
    var i=0;
    theSnake.tiles.forEach(field => {
        if(i!=0){
            var xf = field[0];
            var yf = field[1];
            if(xf==xh&&yf==yh){
                endGame();
                return null;
            }    
        }
        i++;
    })
    ccontext.beginPath();
    ccontext.fillStyle = '#990000';
    ccontext.fillRect(xh1,yh1,20,20);
    ccontext.stroke();
    xt=theSnake.tiles[theSnake.tiles.length-1][0];
    yt=theSnake.tiles[theSnake.tiles.length-1][1];
    xt1=fields[xt][yt].x;
    yt1=fields[xt][yt].y;
    ccontext.beginPath();
    ccontext.fillStyle='#500000';
    ccontext.fillRect(xt1,yt1,20,20);
    ccontext.stroke();
}
drawSnake();
function pressedKey(e) {
    key = e.code;
    firstMove = true;
    if(key=='KeyA'&&(theSnake.d=="n"||theSnake.d=="s")){
        theSnake.d="w";
    }
    if(key=='KeyD'&&(theSnake.d=="n"||theSnake.d=="s")){
        theSnake.d="e";
    }
    if(key=='KeyS'&&(theSnake.d=="w"||theSnake.d=="e")){
        theSnake.d="s";
    }
    if(key=='KeyW'&&(theSnake.d=="w"||theSnake.d=="e")){
        theSnake.d="n";
    }
}
var intervalId = window.setInterval(function(){
    if(firstMove){moveSnake();}
}, 100);

function endGame() {
    clearInterval(intervalId);
    ccontext.fillStyle='#000000';
    ccontext.font='50px Bahnschrift';
    ccontext.fillText("Lost!",150,200); 
}