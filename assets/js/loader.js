const snipper = document.getElementById('page_loader')
const wrapper = document.getElementById('_main')

window.onload = function () {
	fetch('http://127.0.0.1:8000/json-data/')
	.then(res => {
		if(res.ok) {
			setTimeout(()=> {
				snipper.classList.add('hidden')
				wrapper.classList.remove('hidden')
			}, 500)
		}
	})
	.catch(err => {
		console.log('ERR');
	})
}