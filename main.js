const canvas = document.getElementById("mainCanvas")

canvas.height = window.innerHeight
canvas.width = 600

const ctx = canvas.getContext("2d")

const road = new Road(canvas.width / 2, canvas.width * 0.95)
const car = new Car(road.getLaneCenter(4), 100, 30, 50, "KEYS", 4)
const traffic = [
  new Car(road.getLaneCenter(1), -100, 30, 50, "DUMMY", 1.5)
]


animate()

function animate() {
  for (let i = 0; i < traffic.length; i++) {
    traffic[i].update(road.borders, [])
  }
  car.update(road.borders, traffic)
  canvas.height = window.innerHeight

  ctx.save()
  ctx.translate(0, -car.y + canvas.height * 0.75)

  road.draw(ctx)
  for (let i = 0; i < traffic.length; i++) {
    traffic[i].draw(ctx, "blue")
  }
  car.draw(ctx, "yellow")

  ctx.restore()
  requestAnimationFrame(animate)
}