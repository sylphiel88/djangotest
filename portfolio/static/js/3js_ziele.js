import * as THREE from './three.js-master/build/three.module.js'
import { GLTFLoader } from './three.js-master/examples/jsm/loaders/GLTFLoader.js';
const slide_menu = document.querySelectorAll(".sidenav");
M.Sidenav.init(slide_menu, {});
$(document).ready(function(){
    $('.dropdown-trigger').dropdown();  
    $('.collapsible').collapsible();
    console.log("geht");
    // threejstest.init();
        let scene, camera,renderer, hlight,canvas,widthx,heighty,camy,camz;
        function init() {
            widthx = window.innerWidth;
            heighty = window.innerHeight;
            console.log(widthx, heighty);
            if(widthx>1100) {
                canvas = document.getElementById("canvas");
                scene = new THREE.Scene();
                camera = new THREE.PerspectiveCamera(60,widthx/heighty,1,200);
                camy = widthx<1400?150:120;
                camz = widthx<1400?80:40;
                camera.position.y +=camy;
                camera.position.z +=camz; 
                camera.lookAt(0,0,-30);
                hlight = new THREE.AmbientLight(0x80aaaa,3);
                scene.add(hlight);
                renderer=new THREE.WebGL1Renderer({antialias:true,alpha:true});
                renderer.setSize(400,260);
                canvas.appendChild(renderer.domElement);
                let loader = new GLTFLoader();
                loader.load('static/js/ziele.glb', function (gltf) {
                    scene.add(gltf.scene);
                    renderer.render(scene, camera);
                });
            }
        }
        init();
    });