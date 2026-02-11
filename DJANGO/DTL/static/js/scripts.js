/*!
* Start Bootstrap - Grayscale v7.0.5 (https://startbootstrap.com/theme/grayscale)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

var start = new Date().getTime();
function getRandomColor(){
    var letters = '0123456789ABCDEF';
    var color = '#';
    for(var i = 0; i<6; i++){
        color += letters[Math.floor(Math.random()* 16)];
    }
    return color;
}
function move(){
    var left;
    var top;
    var wh;
    left = Math.random() * 300;
    right = Math.random() * 300;
    wh = ((Math.random() * 400) + 100);
    document.getElementById("shape").style.left = left;
    document.getElementById("shape").style.top = top;
    document.getElementById("shape").style.width = wh;
    document.getElementById("shape").style.height = wh;
    document.getElementById("shape").style.display = left;
    var start = new Date().getTime();
}

document.getElementById("shape").onclick = function(){
    document.getElementById("shape").style.display = "block";
    document.getElementById("shape").style.backgroundColor=getRandomColor();
    var end = new Date().getTime();
    var timeTaken = (end-start)/1000;
    alert(timeTaken);
    move();
}