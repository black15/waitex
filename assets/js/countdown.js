// Set the date we're counting down to
var today 		= new Date().getTime();
var deadline 	= document.getElementById('deadline_date')

const event_date = Date.parse(deadline.textContent)

const days_ 	= document.getElementById('days')
const hours_ 	= document.getElementById('hours')
const minutes_ = document.getElementById('minutes')
const seconds_ = document.getElementById('seconds')

var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = event_date - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  days_.innerText = days
  hours_.innerText = hours
  minutes_.innerText = minutes
  seconds_.innerText = seconds

  // if (distance < 0) {
  //   clearInterval(x);
  //   document.getElementById("demo").innerHTML = "EXPIRED";
  // }
}, 1000);