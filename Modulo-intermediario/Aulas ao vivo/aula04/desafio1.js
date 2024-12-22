

document.addEventListener('DOMContentLoaded', (event) => {
    const images = document.querySelectorAll('.carrosel img');
    const leftArrow = document.querySelector('.arrow.left');
    const rightArrow = document.querySelector('.arrow.right');
    let currentImageIndex = 0;

    function showImage(index) {
        images.forEach((img, i) => {
            img.classList.toggle('active', i === index);
        });
    }

    leftArrow.addEventListener('click', () => {
        currentImageIndex = (currentImageIndex > 0) ? currentImageIndex - 1 : images.length - 1;
        showImage(currentImageIndex);
    });

    rightArrow.addEventListener('click', () => {
        currentImageIndex = (currentImageIndex < images.length - 1) ? currentImageIndex + 1 : 0;
        showImage(currentImageIndex);
    });

    showImage(currentImageIndex);
});
