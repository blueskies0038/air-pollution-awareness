window.addEventListener("scroll", function(){
    let myNav = document.querySelector('nav');
    let windowPosition = window.scrollY > innerHeight-200
    myNav.classList.toggle('scrolling-active', windowPosition);
})


const navbarToggler = document.querySelector(".navbar-toggler");
const navbarMenu = document.querySelector(".navbar ul");
const navbarLinks = document.querySelectorAll(".navbar a");

navbarToggler.addEventListener("click", navbarTogglerClick);

function navbarTogglerClick() {
    navbarToggler.classList.toggle("open-navbar-toggler");
    navbarMenu.classList.toggle("open");
}

for(let i=0; i<navbarLinks.length; i++) {
    navbarLinks[i].addEventListener("click", navbarLinkClick);
}

function navbarLinkClick(event) {

    smoothScroll(event);

    if(navbarMenu.classList.contains("open")) {
        navbarToggler.click();
    }

}

function smoothScroll(event) {
    event.preventDefault();
   const targetId = event.currentTarget.getAttribute("href");
   window.scrollTo({
     top: targetId==="#" ? 0 : document.querySelector(targetId).offsetTop,
     behavior: "smooth"
   });
 }



