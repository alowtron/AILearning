const canvas = document.getElementById("mainCanvas")

canvas.height = window.innerHeight
canvas.width = 600

const ctx = canvas.getContext("2d")

const road = new Road(canvas.width / 2, canvas.width * 0.95)
const car = new Car(road.getLaneCenter(4), 100, 30, 50)
car.update()
car.draw(ctx)

animate()

function animate() {
  car.update()
  canvas.height = window.innerHeight

  ctx.save()
  ctx.translate(0, -car.y + canvas.height * 0.75)
  road.draw(ctx)
  car.draw(ctx)
  ctx.restore()
  requestAnimationFrame(animate)
}