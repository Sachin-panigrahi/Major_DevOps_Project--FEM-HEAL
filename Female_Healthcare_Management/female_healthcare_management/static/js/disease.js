document.addEventListener("DOMContentLoaded", function() {
    const moreButtons = document.querySelectorAll(".more-button");
    const popup = document.querySelector(".popup");
    const closeButtons = document.querySelectorAll(".close-popup");
    const showMoreButtons = document.querySelectorAll(".show-more");

    moreButtons.forEach(button => {
        button.addEventListener("click", function() {
            const disease = this.getAttribute("data-disease");
            document.querySelectorAll(".disease-detail").forEach(detail => {
                detail.style.display = "none";
            });
            document.getElementById(disease).style.display = "block";
            popup.style.display = "flex";
        });
    });

   
    closeButtons.forEach(button => {
        button.addEventListener("click", function() {
            popup.style.display = "none";
        });
    });

    showMoreButtons.forEach(button => {
        button.addEventListener("click", function() {
            const disease = this.getAttribute("data-disease");
            const moreContent = document.querySelector(`.more-content[data-disease="${disease}"]`);
            if (moreContent.classList.contains("show")) {
                moreContent.classList.remove("show");
                this.textContent = "Show More";
            } else {
                moreContent.classList.add("show");
                this.textContent = "Show Less";
            }
        });
    });

    const sliders = document.querySelectorAll(".slider");

    sliders.forEach(slider => {
        let slides = slider.querySelector(".slides");
        let images = slides.querySelectorAll("img");
        let index = 0;

        setInterval(() => {
            index = (index + 1) % images.length;
            slides.style.transform = `translateX(${-index * 100}%)`;
        }, 3000);
    });
});
