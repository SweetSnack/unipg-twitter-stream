function Ball(color, x, y, destination) {
  Vector2D.call(this, x, y);
  this.color = color;
  this.speed = 5;
  this.radius = 10;
  this.text = destination || '';
  this.destination = destination;
}

Ball.prototype = new Vector2D();

Ball.prototype.move = function () {

  // if ball has no destination
  if (!this.destination) {
    // nothing to do here
    return true;
  }

  var vect = this.destination.minus(this);
  var distance = vect.length();

  // destination reached
  if (distance === 0) {
    this.destination.getFed && this.destination.getFed();
    this.destination = null;
    // say goodbye to this world!
    return false;
  }

  // last movement
  if (distance < this.speed) {
    this.setTo(this.destination);
    return true;
  }

  vect.normalize();
  vect.scale(this.speed);

  this.add(vect);

  return true;
};

Ball.prototype.draw = function (context) {
  context.beginPath();
  context.arc(this.x, this.y, this.radius, 0, 2 * Math.PI, false);
  context.fillStyle = this.color;
  context.fill();
  context.font="20px Georgia";
  context.fillStyle = 'black';
  context.fillText(this.text, this.x - this.text.length/2 * 9, this.y + this.radius + 23);
  context.lineWidth = 3;
  context.strokeStyle = '#003300';
  context.stroke();
};

Ball.prototype.getFed = function () {
  this.radius++;
};

Ball.prototype.constructor = Ball;