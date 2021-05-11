/*!
* Start Bootstrap - Simple Sidebar v5.2.0 (https://startbootstrap.com/template/simple-sidebar)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-simple-sidebar/blob/master/LICENSE)
*/
// Toggles the sidebar

$("#menu-toggle").click(function (e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

function openTab(evt, whichTab) {
    var i, tabContent, tabLinks;
    tabContent = document.getElementsByClassName("tabcontent");
    for (i=0; i < tabContent.length; i++){
        tabContent[i].style.display = "none";
    }
    tabLinks = document.getElementsByClassName("tabLinks");
    for (i=0; i < tabLinks.length; i++){
        tabLinks[i].className = tabLinks[i].className.replace(" active", "");
    }
    document.getElementById(whichTab).style.display = "block";
    evt.currentTarget.className += " active";
}
