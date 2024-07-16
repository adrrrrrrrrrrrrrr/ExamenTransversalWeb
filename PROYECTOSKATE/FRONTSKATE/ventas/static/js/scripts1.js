
let slideIndex = 1;

function moveSlide(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    let i;
    const slides = document.getElementsByClassName("slide");
    if (n > slides.length) {slideIndex = 1}    
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slides[slideIndex-1].style.display = "block";  
}




document.addEventListener('DOMContentLoaded', function() {
    const searchBox = document.getElementById('search-box');
    const searchButton = document.querySelector('.search-button');

    // Mostrar el campo de búsqueda cuando se hace clic en el botón de búsqueda
    searchButton.addEventListener('click', function(event) {
        event.preventDefault(); // Previene la acción predeterminada del botón (por ejemplo, enviar un formulario)
        searchBox.style.display = 'block';
    });

    // Ocultar el campo de búsqueda cuando se hace clic fuera de él
    document.addEventListener('click', function(event) {
        if (!searchBox.contains(event.target) && event.target !== searchButton) {
            searchBox.style.display = 'none';
        }
    });
});




