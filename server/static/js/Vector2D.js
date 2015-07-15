function Vector2D(x, y) {
  this.x = x || 0;
  this.y = y || 0;
}

Vector2D.prototype = {
  setTo: function (vector) {
    this.x = vector.x;
    this.y = vector.y;
  },
  add: function (vector) {
    this.x += vector.x;
    this.y += vector.y;
  },
  scale: function (scalar) {
    this.x *= scalar;
    this.y *= scalar;
  },
  minus: function (vector) {
    return new Vector2D(this.x - vector.x, this.y - vector.y);
  },
  length: function () {
    return Math.sqrt(this.x * this.x + this.y * this.y);
  },
  normalize: function() {
    var length = this.length();
    this.x /= length;
    this.y /= length;
  }
};