let canvas = document.querySelector('#canvas')
let c = canvas.getContext('2d')

let limit_x = window.innerWidth, limit_y = window.innerHeight
canvas.width = limit_x
canvas.height = limit_y
canvas.style.backgroundColor = '#2C3E50'

let mouse = {
	x: 0, y: 0
}

let colors = [
	'#2C3E50',
	'#E74C3C',
	'silver',
	'#3498DB',
	'#2980B9'
]

window.addEventListener('resize', function(){
	limit_x = window.innerWidth
	limit_y = window.innerHeight
	canvas.width = limit_x
	canvas.height = limit_y
	
	init()
})

window.addEventListener('mousemove', function(event){
	mouse.x = event.x
	mouse.y = event.y
})

function Circle(x, y, radius, dx, dy){
	this.x = x
	this.y = y
	this.radius = radius
	this.maxRadius = this.radius * 10
	this.minRadius = radius
	this.dx = dx
	this.dy = dy
	this.color = colors[parseInt(Math.random() * colors.length)]

	this.draw = function(){
		c.beginPath()
		c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false)
		c.fillStyle = this.color
		c.fill()
	}

	this.update = function(){
		if(this.x - this.radius < 0 || this.x + this.radius > limit_x){
			this.dx = -this.dx
		}
		if(this.y - this.radius < 0 || this.y + this.radius > limit_y){
			this.dy = -this.dy
		}
		this.x += this.dx	
		this.y += this.dy

		if(Math.abs(this.x - mouse.x) < 50 && Math.abs(this.y - mouse.y ) < 50){
			this.radius = this.maxRadius
		}else{
			this.radius = this.minRadius
		}
		this.draw()
	}
}

let circles = []
function init(){
	circles = []

	for(let i = 0; i < 1000; i++){
		let x = Math.random() * limit_x
		let y = Math.random() * limit_y
		let dx = (Math.random() - 0.8)
		let dy = (Math.random() - 0.5)
		let radius = Math.random() * 2

		circle = new Circle(x, y, radius, dx, dy)
		circles.push(circle)
	}
}

init()

function animate(){
	requestAnimationFrame(animate)
	c.fillStyle = '#2C3E50'
	c.fillRect(0, 0, limit_x, limit_y)
	circles.forEach((circle) =>{
		circle.update()
	})
}

animate()
