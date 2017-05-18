var header = document.querySelector("#siteWrapper header");

function scrolled() {
  var windowHeight = document.body.clientHeight,
    currentScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var headerHeight = header.offsetHeight;

  header.className = (currentScroll >= windowHeight - header.offsetHeight) ? "fixed" : "";
  //le header devient fixe
}

addEventListener("scroll", scrolled, false);
