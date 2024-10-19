import intlTelInput from 'intl-tel-input';
import 'intl-tel-input/build/css/intlTelInput.css';

// Initialize phone input
const phoneInputField = document.querySelector("#phone");
const iti = intlTelInput(phoneInputField, {
  utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});

// Submit phone number for verification
document.querySelector("#sendCode").addEventListener("click", function() {
  const phoneNumber = iti.getNumber();
  
  // Make an AJAX request to send the phone number to Django backend
  fetch("/send-verification-code/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"), // Ensure CSRF protection
    },
    body: JSON.stringify({ phone_number: phoneNumber }),
  }).then(response => response.json()).then(data => {
    if (data.success) {
      // Handle successful response
      alert("Verification code sent!");
    } else {
      alert("Error sending verification code");
    }
  });
});

// CSRF token helper
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
