const mainCanvas = document.getElementById("mainCanvas")

const networkCanvas = document.getElementById("networkCanvas")
networkCanvas.width = 600

// mainCanvas.height = window.innerHeight
mainCanvas.width = 600

const mainCtx = mainCanvas.getContext("2d")
const networkCtx = networkCanvas.getContext("2d")

const road = new Road(mainCanvas.width / 2, mainCanvas.width * 0.95)
// const car = new Car(road.getLaneCenter(4), 100, 30, 50, "AI", 4)
const numberOfCars = 1000
const cars = generateCars(numberOfCars)

let bestCar = cars[0]
if (localStorage.getItem("bestBrain")) {
  for (let i = 0; i < cars.length; i++) {
    cars[i].brain = JSON.parse(
      localStorage.getItem("bestBrain")
    )
    if (i != 0) {
      NeuralNetwork.mutate(cars[i].brain, 0.3)
    }
  }
  
}

const traffic = [
  new Car(road.getLaneCenter(4), -100, 30, 50, "DUMMY", 1.5),
  new Car(road.getLaneCenter(3), -700, 30, 50, "DUMMY", 1.5),
  new Car(road.getLaneCenter(2), -1100, 30, 50, "DUMMY", 1.5),
  // new Car(road.getLaneCenter(2), -700, 30, 50, "DUMMY", 1.5),
  new Car(road.getLaneCenter(1), -1100, 30, 50, "DUMMY", 1.5),
  new Car(road.getLaneCenter(3), -1555, 30, 50, "DUMMY", 1.5),
  new Car(road.getLaneCenter(1), -1111, 30, 50, "DUMMY", 1.5),

  new Car(road.getLaneCenter(4), 500, 30, 50, "DUMMY", 1.5),
  new Car(road.getLaneCenter(3), 700, 30, 50, "DUMMY", 1.5),
  new Car(road.getLaneCenter(1), 1100, 30, 50, "DUMMY", 1.5),
]


animate()

function generateCars(numberOfCars) {
  const cars = []
  for (let i = 0; i < numberOfCars; i++) {
    cars.push(new Car(road.getLaneCenter(2), 100, 30, 50, "AI", 4))
  }
  return cars
}

function save() {
  localStorage.setItem("bestBrain",
    JSON.stringify(bestCar.brain)
  )
}

function discard() {
  localStorage.removeItem("bestBrain")
}

function animate() {
  for (let i = 0; i < traffic.length; i++) {
    traffic[i].update(road.borders, [])
  }
  for (let i = 0; i < cars.length; i++) {
    cars[i].update(road.borders, traffic)
  }

  bestCar =  cars.find(
    c => c.y == Math.min(
      ...cars.map(c => c.y)
    )
  )
  // car.update(road.borders, traffic)
  mainCanvas.height = window.innerHeight
  networkCanvas.height = window.innerHeight


  mainCtx.save()
  mainCtx.translate(0, -bestCar.y + mainCanvas.height * 0.75)

  road.draw(mainCtx)
  for (let i = 0; i < traffic.length; i++) {
    traffic[i].draw(mainCtx, "blue")
  }
  mainCtx.globalAlpha = 0.1
  for (let i = 0; i < cars.length; i++) {
    cars[i].draw(mainCtx, "yellow")
  }
  mainCtx.globalAlpha = 1
  bestCar.draw(mainCtx, "yellow", true)
  // car.draw(mainCtx, "yellow")

  mainCtx.restore()

  Visualizer.drawNetwork(networkCtx, bestCar.brain)
  requestAnimationFrame(animate)
}