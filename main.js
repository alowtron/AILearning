const mainCanvas = document.getElementById("mainCanvas")

const networkCanvas = document.getElementById("networkCanvas")
networkCanvas.width = 600

// mainCanvas.height = window.innerHeight
mainCanvas.width = 600

const mainCtx = mainCanvas.getContext("2d")
const networkCtx = networkCanvas.getContext("2d")

const road = new Road(mainCanvas.width / 2, mainCanvas.width * 0.95)
// const car = new Car(road.getLaneCenter(4), 100, 30, 50, "AI", 4)
const numberOfCars = 100
const cars = generateCars(numberOfCars)
const traffic = [
  new Car(road.getLaneCenter(1), -100, 30, 50, "DUMMY", 1.5)
]


animate()

function generateCars(numberOfCars) {
  const cars = []
  for (let i = 0; i < numberOfCars; i++) {
    cars.push(new Car(road.getLaneCenter(4), 100, 30, 50, "AI", 4))
  }
  return cars
}

function animate() {
  for (let i = 0; i < traffic.length; i++) {
    traffic[i].update(road.borders, [])
  }
  for (let i = 0; i < cars.length; i++) {
    cars[i].update(road.borders, traffic)
  }
  // car.update(road.borders, traffic)
  mainCanvas.height = window.innerHeight
  networkCanvas.height = window.innerHeight


  mainCtx.save()
  mainCtx.translate(0, -cars[0].y + mainCanvas.height * 0.75)

  road.draw(mainCtx)
  for (let i = 0; i < traffic.length; i++) {
    traffic[i].draw(mainCtx, "blue")
  }
  for (let i = 0; i < cars.length; i++) {
    cars[i].draw(mainCtx, "yellow")
  }
  // car.draw(mainCtx, "yellow")

  mainCtx.restore()

  Visualizer.drawNetwork(networkCtx, cars[0].brain)
  requestAnimationFrame(animate)
}