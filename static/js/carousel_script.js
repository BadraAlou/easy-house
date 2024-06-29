const carousel = document.querySelector('#introCarousel');
const interval = 3000;
let autoScrollInterval;

// Function to scroll the carousel
function scrollCarousel() {
  const currentSlide = carousel.querySelector('.carousel-item.active');
  const nextSlide = currentSlide.nextElementSibling;

  if (nextSlide) {
    // Scroll to the next slide
    carousel.querySelector('.carousel-control-next').click();
  } else {
    // Loop back to the first slide
    carousel.querySelector('.carousel-control-prev').click();
  }
}

// Function to start automatic scrolling
function startAutoScroll() {
  autoScrollInterval = setInterval(scrollCarousel, interval);
}

// Function to stop automatic scrolling
function stopAutoScroll() {
  clearInterval(autoScrollInterval);
}

// Set interval for automatic scrolling
startAutoScroll();

// Select all search inputs inside the carousel
const searchInputs = carousel.querySelectorAll('.form-control');

// Add event listeners for input and blur on search inputs
searchInputs.forEach(function(input) {
  input.addEventListener('input', function() {
    // If user is typing in the search input, stop auto scrolling
    stopAutoScroll();
  });

  input.addEventListener('blur', function() {
    // If user is done typing and the input loses focus, start auto scrolling again
    startAutoScroll();
  });
});
