class Car {
  constructor(x, y, width, height) {
    this.x = x
    this.y = y
    this.width = width
    this.height = height

    this.controls = new Controls()

    this.speed = 0
    this.maxSpeed = 2
    this.acceleration= this.maxSpeed / 10
    this.friction = this.maxSpeed / 40
  }

  update() {
    if (this.controls.forward) {
      this.speed -= this.acceleration
    }
    if (this.controls.reverse) {
      this.speed += this.acceleration
    }
    if (this.speed > this.maxSpeed) {
      this.speed = this.maxSpeed
    } else if (this.speed < -this.maxSpeed) {
      this.speed = -this.maxSpeed
    }
    if (this.speed > 0) {
      this.speed -= this.friction
    } else if (this.speed < 0) {
      this.speed += this.friction
    }
    this.y += this.speed
    if (this.controls.left) {
      this.x -= this.maxSpeed
    }
    if (this.controls.right) {
      this.x += this.maxSpeed
    }
  }
  draw(ctx) {
    ctx.beginPath()
    ctx.rect(
      this.x - this.width / 2,
      this.y - this.height / 2,
      this.width,
      this.height,
    )
    ctx.fill()
  }
}