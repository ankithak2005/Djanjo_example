const box = document.getElementById('mouseBox');
let isClicked = false;

// Move box with mouse
document.addEventListener('mousemove', (e) => {
  const x = e.clientX;
  const y = e.clientY;
  box.style.left = `${x - box.offsetWidth / 2}px`;
  box.style.top = `${y - box.offsetHeight / 2}px`;

  if (!isClicked) {
    // Slight rotation effect based on mouse speed
    box.style.transform = `rotate(${(x + y) % 30 - 15}deg)`;
  }
});

// Handle click - toggle color
document.addEventListener('mousedown', () => {
  isClicked = true;
  box.classList.add('clicked');
});

document.addEventListener('mouseup', () => {
  isClicked = false;
  box.classList.remove('clicked');
});
