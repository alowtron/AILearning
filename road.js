class Road {
  constructor (x, width, laneCount = 9) {
    this.x = x
    this.width = width
    this.laneCount = laneCount

    this.left = x - width/2
    this.right = x + width/2

    const infinity = 9999999
    this.top = -infinity
    this.bottom = infinity


    const topLeft = { x: this.left, y: this.top }
    const bottomLeft = { x: this.left, y: this.bottom }
    const topRight = { x: this.right, y: this.top }
    const bottomRight = { x: this.right, y: this.bottom }
    this.border = [
      [
        topLeft, bottomLeft
      ],
      [
        topRight, bottomRight
      ]
    ]
  }

  getLaneCenter(laneIndex) {
    const laneWidth = this.width / this.laneCount
    return this.left + laneWidth / 2 + laneIndex * laneWidth
  }

  draw(ctx) {
    ctx.lineWidth = 3
    ctx.strokeStyle = "white"

    for (let i=1; i <=this.laneCount - 1; i++) {
      const x = lerp(
        this.left,
        this.right,
        i/this.laneCount
      )

      ctx.setLineDash([20, 20])
      ctx.beginPath()
      ctx.moveTo(x, this.top)
      ctx.lineTo(x, this.bottom)
      ctx.stroke()
    }
    ctx.setLineDash([])
    this.border.forEach(border => {
      ctx.beginPath()
      ctx.moveTo(border[0].x, border[0].y)
      ctx.lineTo(border[1].x, border[1].y)
      ctx.stroke()
    })
    
  }
  
  
}

