document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const inputs = form.querySelectorAll('input');
  
    inputs.forEach(input => {
      input.addEventListener('focus', () => {
        input.style.borderColor = '#00796b';
      });
  
      input.addEventListener('blur', () => {
        input.style.borderColor = '#ccc';
      });
    });
  
    form.addEventListener('submit', () => {
      form.classList.add('submitting');
    });
  });