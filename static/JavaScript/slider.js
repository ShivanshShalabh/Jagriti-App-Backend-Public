let active_slide = 0;
let carousel_item = document.getElementsByClassName('carousel-item');
const label = document.getElementsByClassName('label-btn');
const nxtbtn = document.getElementsByClassName('carousel-control-next');
const prevbtn = document.getElementsByClassName('carousel-control-prev');

// Next slide function

const next_slide = () => {
    for (let j = 0; j < carousel_item.length; j++) {
        if (carousel_item[j].classList.contains('active')) {
            carousel_item[j].classList.remove('active');
            label[j].classList.remove('active');
            carousel_item[(j + 1) % 5].classList.add('active');
            label[(j + 1) % 5].classList.add('active');
            break;
        }
    }
};

// Next btn click function

nxtbtn[0].addEventListener('click', next_slide);

// Prev btn click function

prevbtn[0].addEventListener('click', () => {
    for (let j = 0; j < carousel_item.length; j++) {
        if (carousel_item[j].classList.contains('active')) {
            carousel_item[j].classList.remove('active');
            label[j].classList.remove('active');
            if (j != 0) {
                carousel_item[(j - 1)].classList.add('active');
                label[(j - 1)].classList.add('active');
            }

            else {
                carousel_item[(carousel_item.length - 1)].classList.add('active');
                label[(carousel_item.length - 1)].classList.add('active');
            }

            break;
        }
    }
});

// Label click function

for (let i = 0; i < label.length; i++) {
    label[i].addEventListener('click', () => {
        for (let j = 0; j < carousel_item.length; j++) {
            if (carousel_item[j].classList.contains('active')) {
                carousel_item[j].classList.remove('active');
                label[j].classList.remove('active');
            }
        }

        let index = label[i].getAttribute('data-slide-to');
        label[index].classList.add('active');
        carousel_item[index].classList.add('active');
    }
    );
};

setInterval(next_slide, 5000);

// Slider display toggle

const toggle_slider_transition = () => {
    document.getElementById('carouselExampleIndicators').classList.toggle('slider_transition');
};

let counter_slider = 1;
document.getElementById('toggle_btn').addEventListener('click', () => {
    if (counter_slider % 2 != 0) {
        document.getElementById('carouselExampleIndicators').style.transition = 'all 0s !important';
        document.getElementById('carouselExampleIndicators').style.opacity = '0';
        document.getElementById('carouselExampleIndicators').style.zIndex = '-1';
        if (counter_slider != 1)
            toggle_slider_transition();
    }

    else {
        setTimeout(() => {
            toggle_slider_transition();
            document.getElementById('carouselExampleIndicators').style.transition = 'all 0.5s !important';
            document.getElementById('carouselExampleIndicators').style.opacity = '1';
            document.getElementById('carouselExampleIndicators').style.zIndex = '0';
        }, 200);
    }

    counter_slider++;
});

let counter_slider_profile = 1;
document.getElementById('profile_toggle').addEventListener('click', () => {
    if (counter_slider_profile % 2 != 0) {
        document.getElementById('carouselExampleIndicators').style.transition = 'all 0s !important';
        document.getElementById('carouselExampleIndicators').style.opacity = '0';
        document.getElementById('carouselExampleIndicators').style.zIndex = '-1';
        if (counter_slider_profile != 1)
            toggle_slider_transition();
    }

    else {
        setTimeout(() => {
            toggle_slider_transition();
            document.getElementById('carouselExampleIndicators').style.transition = 'all 0.5s !important';
            document.getElementById('carouselExampleIndicators').style.opacity = '1';
            document.getElementById('carouselExampleIndicators').style.zIndex = '0';
        }, 200);
    }

    counter_slider_profile++;
});
