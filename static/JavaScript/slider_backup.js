const carouselslide = document.querySelector(".carousel-slide");
const carouselImages = document.querySelectorAll(".carousel-slide img");
const radbtn = document.querySelectorAll(".slider-radio input");
const prevbtn = document.querySelector("#slider-prev-btn");
const nxtbtn = document.querySelector("#slider-nxt-btn");
let counter = 1;
glow(counter);
let size;
size_init();
carouselslide.style.transform = "translateX(" + -size * counter + "px)";
function size_init() {
    size = carouselImages[0].clientWidth;
}

carouselslide.style.transform = "translateX(" + -size * counter + "px)";
nxtbtn.addEventListener("click", () => {
    if (counter >= carouselImages.length - 1) return;
    carouselslide.style.transition = "transform 0.4s ease-in-out";
    counter++;
    carouselslide.style.transform = "translateX(" + -size * counter + "px)";
    glow(counter);
    size_init();
});
prevbtn.addEventListener("click", () => {
    if (counter <= 0) return;
    carouselslide.style.transition = "transform 0.4s ease-in-out";
    counter--;
    carouselslide.style.transform = "translateX(" + -size * counter + "px)";
    glow(counter);
    size_init();
});
carouselslide.addEventListener("transitionend", () => {
    if (carouselImages[counter].id == "lastClone") {
        carouselslide.style.transition = "none";
        counter = carouselImages.length - 2;
        carouselslide.style.transform = "translateX(" + -size * counter + "px)";
    }

    if (carouselImages[counter].id == "firstClone") {
        carouselslide.style.transition = "none";
        counter = carouselImages.length - counter;
        carouselslide.style.transform = "translateX(" + -size * counter + "px)";
    }

    glow(counter);
    size_init();
});
function slide() {
    if (counter >= carouselImages.length - 1) return;
    carouselslide.style.transition = "transform 0.4s ease-in-out";
    counter++;
    carouselslide.style.transform = "translateX(" + -size * counter + "px)";
    glow(counter);
    size_init();
}

function glow(num) {
    if (num == 0) {
        const temp = radbtn[0].id;
        document.getElementById(temp).checked = true;
    } else if (num > 5) {
        const temp = radbtn[4].id;
        document.getElementById(temp).checked = true;
    } else {
        const temp = radbtn[num - 1].id;
        document.getElementById(temp).checked = true;
    }
}

setInterval(slide, 5000);
$(document).ready(function () {
    $(".slider-radio").click(function () {
        if (document.getElementById("sl-btn1").checked) {
            rad_fun(1);
        } else if (document.getElementById("sl-btn2").checked) {
            rad_fun(2);
        } else if (document.getElementById("sl-btn3").checked) {
            rad_fun(3);
        } else if (document.getElementById("sl-btn4").checked) {
            rad_fun(4);
        } else if (document.getElementById("sl-btn5").checked) {
            rad_fun(5);
        }
    });
});
function pos(xyz) {
    if (xyz < 0) return -1 * xyz;
    else return xyz;
}

function rad_fun(n) {
    let last = counter;
    counter = n;
    carouselslide.style.transition =
        "transform" + String(0.4 * pos(last - counter)) + "s ease-in-out";
    carouselslide.style.transform = "translateX(" + -size * counter + "px)";
}

window.addEventListener("load", size_init, false);
