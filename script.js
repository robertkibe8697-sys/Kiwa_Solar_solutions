document.addEventListener("DOMContentLoaded", () => {
  const hamburger = document.getElementById("menu-toggle");
  const navLinks = document.getElementById("navLinks");

  hamburger.addEventListener("click", () => {
    console.log("clicked");
    navLinks.classList.toggle("active");
  });
});