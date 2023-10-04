// Get the HTML element that contains the customer input.
const inputElement = document.getElementById('customer-input');

// Validate the input value.
const isValidInput = /^[a-zA-Z]+$/.test(inputElement.value);

// If the input value is invalid, display an error message to the customer and prevent them from submitting the form.
if (!isValidInput) {
  alert('The customer input must contain only letters.');
  return false;
}

// Allow the customer to submit the form.
return true;
