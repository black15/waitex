const cart = document.getElementById('cart')
const cart_wrapper = document.getElementById('cart_wrapper')

function slideIn(e) {
	cart.classList.add('slide-in')
	cart.classList.remove('hidden')
}

function slideOut(e) {
	cart.classList.add('hidden')
	cart_wrapper.classList.add('slide-out')
}