document.addEventListener('DOMContentLoaded', function() {
	const quantityInput = document.getElementById('quantity');
	const decrementButton = document.getElementById('decrement');
	const incrementButton = document.getElementById('increment');
	
	decrementButton.addEventListener('click', function() {
	  if (quantityInput.value > 1) {
		 quantityInput.value--;
	  }
	});
	
	incrementButton.addEventListener('click', function() {
	  quantityInput.value++;
	});
 });