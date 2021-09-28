// ----------------------- Scroll to top button -----------------------

let topbutton = document.getElementById("goToTopBtn");

window.onscroll = function() {scrollPage();};

function scrollPage() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    topbutton.style.display = "block";
  } else {
    topbutton.style.display = "none";
  }
}

function goToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}