const slide_menu = document.querySelectorAll(".sidenav");
M.Sidenav.init(slide_menu, {});
$(document).ready(function(){
    $('.dropdown-trigger').dropdown();  
    $('.collapsible').collapsible();
    console.log("geht");
    // threejstest.init();
});