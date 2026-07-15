window.addEventListener("scroll", function () {

    const navbar = document.getElementById("mainNavbar");

    if (window.scrollY > 50) {

        navbar.classList.add("scrolled");

    } else {

        navbar.classList.remove("scrolled");

    }

});

/*==========================
BACK TO TOP
===========================*/

const backToTop = document.getElementById("backToTop");

window.addEventListener("scroll", () => {

    if(window.scrollY > 300){

        backToTop.classList.add("show");

    }else{

        backToTop.classList.remove("show");

    }

});

backToTop.addEventListener("click", () => {

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

});

/*==========================
GALLERY FILTER
===========================*/

const filterButtons = document.querySelectorAll(".filter-btn");
const galleryItems = document.querySelectorAll(".gallery-item");
const galleryCount = document.getElementById("galleryCount");

filterButtons.forEach(button => {

    button.addEventListener("click", () => {

        filterButtons.forEach(btn => btn.classList.remove("active"));

        button.classList.add("active");

        const filter = button.dataset.filter;

        let visibleItems = 0;

    galleryItems.forEach(item => {

        if (filter === "all" || item.dataset.category === filter) {

          visibleItems++;

          item.style.display = "";

           setTimeout(() => {

              item.style.opacity = "1";
              item.style.transform = "scale(1)";

        }, 10);

    }

    else {

        item.style.opacity = "0";
        item.style.transform = "scale(.9)";

        setTimeout(() => {

            item.style.display = "none";

        }, 300);

    }

});

galleryCount.textContent = visibleItems;

    });

});

/*==========================
PREMIUM COUNTER ANIMATION
==========================*/

const counters = document.querySelectorAll(".counter");

let counterStarted = false;

function animateCounters() {

    counters.forEach(counter => {

        const targetText = counter.dataset.target;

        const target = parseInt(targetText.replace(/\D/g, ""));

        const duration = 2000; // 2 seconds

        let start = null;

        function update(timestamp) {

            if (!start) start = timestamp;

            const progress = Math.min((timestamp - start) / duration, 1);

            // Ease Out Animation
            const eased = 1 - Math.pow(1 - progress, 3);

            const current = Math.floor(eased * target);

            if (targetText.includes("%")) {

                counter.textContent = current + "%";

            }

            else if (targetText.includes("+")) {

                counter.textContent = current + "+";

            }

            else {

                counter.textContent = current;

            }

            if (progress < 1) {

                requestAnimationFrame(update);

            }

            else {

                counter.textContent = targetText;

            }

        }

        requestAnimationFrame(update);

    });

}

window.addEventListener("scroll", () => {

    const section = document.querySelector("#about");

    if (!section) return;

    const top = section.getBoundingClientRect().top;

    if (top < window.innerHeight - 150 && !counterStarted) {

        animateCounters();

        counterStarted = true;

    }

});

/*==========================
GLIGHTBOX
===========================*/
