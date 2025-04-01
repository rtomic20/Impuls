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

  // 👁 Toggle password visibility
  const togglePassword = document.getElementById('toggle-password');
  const passwordInput = document.getElementById('password');

  togglePassword.addEventListener('click', () => {
    const isVisible = passwordInput.type === 'text';
    passwordInput.type = isVisible ? 'password' : 'text';
    togglePassword.classList.toggle('fa-eye');
    togglePassword.classList.toggle('fa-eye-slash');
  });
});
