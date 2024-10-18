let menu = document.getElementById('menubar')

function openMenu(){
    menu.style.right = '0'
};

function closeMenu(){
    menu.style.right = '-240px'
};

// Get all <details> elements on the page
const details = document.querySelectorAll("details");

// Add event listeners to each <details> element
details.forEach((detail) => {
    detail.addEventListener("click", function () {
        // Close all other <details> elements when one is opened
        details.forEach((otherDetail) => {
            if (otherDetail !== detail) {
                otherDetail.removeAttribute("open");
            }
        });
    });
});
