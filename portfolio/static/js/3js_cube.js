import * as THREE from './three.js-master/build/three.module.js'
$(document).ready(function(){
let scene, camera,renderer, hlight,canvas,widthx,heighty,geometry,material,cube;
function init() {
    widthx = 300;
    heighty = 300;
    canvas = document.getElementById("canvas1");
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(60,widthx/heighty,0.1,1000);
    renderer = new THREE.WebGL1Renderer({antialias:true,alpha:true});
    renderer.setSize(300,300);
    canvas.appendChild(renderer.domElement);
    var texture1 = new THREE.TextureLoader().load('pics/right.png');   
    var texture2 = new THREE.TextureLoader().load('pics/left.png');
    var texture3 = new THREE.TextureLoader().load('pics/top.png');
    var texture4 = new THREE.TextureLoader().load('pics/bottom.png');
    var texture5 = new THREE.TextureLoader().load('pics/back.png');
    var texture6 = new THREE.TextureLoader().load('pics/front.png');
    material = [
        new THREE.MeshBasicMaterial({
            map: texture1 //left
        }),
        new THREE.MeshBasicMaterial({
            map: texture2
        }),
        new THREE.MeshBasicMaterial({
            map: texture3
        }),
        new THREE.MeshBasicMaterial({
            map: texture4
        }),
        new THREE.MeshBasicMaterial({
            map: texture6
        }),
        new THREE.MeshBasicMaterial({
            map: texture5
        })
    ];
	geometry = new THREE.BoxGeometry(2,2,2);
    cube = new THREE.Mesh(geometry,material);
    scene.add(cube);
    scene.add(hlight);
    camera.position.z = 5;
    cube.rotation.x=0.39269908169;
    cube.rotation.y=0.78539816339;
    renderer.render(scene, camera);
    function animatex() {
        cube.rotation.x=    
        renderer.render(scene,camera);
    }
    function animatey() {
        cube.rotation.y=Math.PI*(document.getElementById("inp2").value/360);
        renderer.render(scene,camera);
    }
    function animatez() {
        cube.rotation.z=Math.PI*(document.getElementById("inp3").value/360);
        renderer.render(scene,camera);
    }
    $("#inp1").on("input change",function() {
        document.getElementById("value1").innerHTML=document.getElementById("inp1").value;
        animatex();
    });
    $("#inp2").on("input change",function() {
        document.getElementById("value2").innerHTML=document.getElementById("inp2").value;
        animatey();
    });
    $("#inp3").on("input change",function() {
        document.getElementById("value3").innerHTML=document.getElementById("inp3").value;
        animatez();
    });
}
init();
});