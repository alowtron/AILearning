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
    this.friction = this.maxSpeed / 30

    this.angle = 0
    this.rotateSpeed = 0.02
  }

  update() {
    this.#move()
    
  }

  #move() {
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
      if (this.speed < this.friction && this.speed > -this.friction) {
        this.speed = 0
      }
      
      if (this.speed != 0 ) {
        const flip = this.speed > 0 ? -1 : 1
        if (this.controls.left) {
          this.angle += this.rotateSpeed * flip
        }
        if (this.controls.right) {
          this.angle -= this.rotateSpeed * flip
        }
      }

      this.x += Math.sin(this.angle) * this.speed
      this.y += Math.cos(this.angle) * this.speed
    }

  draw(ctx) {
    ctx.save()
    ctx.translate(this.x, this.y)
    ctx.rotate(-this.angle)
    ctx.beginPath()
    ctx.rect(
      - this.width / 2,
      - this.height / 2,
      this.width,
      this.height,
    )
    ctx.fill()
    ctx.restore()
  }
}