const update_btns = document.getElementsByClassName('update-cart');

for (let index = 0; index < update_btns.length; index++) {
	update_btns[index].addEventListener('click',function() {
		var product_slug = this.dataset.product;
		var action = this.dataset.action;
		if (user === 'AnonymousUser') {
			console.log('You are not logged in');
		}
		else {
			updateUserOrder(product_slug, action)
		}
	})
	
}

function updateUserOrder(product_slug, action) {
	console.log('Initiating ...');
	fetch('update_item/',{
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		mode: 'same-origin',
		body: JSON.stringify({'product_slug': product_slug, 'action': action})
	})
		.then((res) => {
			return res.json()
		})
		.then((data) => {
			console.log('data', data);
		})
}