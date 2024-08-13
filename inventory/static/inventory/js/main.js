function openDrawer() {
  document.getElementById("myDrawer").classList.toggle("active");
}

function closeDrawer() {
  document.getElementById("myDrawer").classList.toggle("active");
}



const swiperWrapper = document.querySelector('.swiper-wrapper');
const slides = document.querySelectorAll('.swiper-slide');
let currentIndex = 0;

function slideNext() {
  currentIndex = (currentIndex + 1) % slides.length;
  updateSlidePosition();
}

function updateSlidePosition() {
  swiperWrapper.style.transform = `translateX(-${currentIndex * 100}%)`;
}

// Auto slide every 3 seconds
setInterval(slideNext, 4000);



