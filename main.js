const canvas = document.getElementById("mainCanvas")

canvas.height = window.innerHeight
canvas.width = 600

const ctx = canvas.getContext("2d")

const car = new Car(300, 100, 30, 50)
car.draw(ctx)

animate()

function animate() {
  car.update()
  canvas.height = window.innerHeight
  car.draw(ctx)
  requestAnimationFrame(animate)
}