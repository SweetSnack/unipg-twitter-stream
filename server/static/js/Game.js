var canvas = document.getElementById('myCanvas');

function makeCanvasFullPage() {
  canvas.width = document.documentElement.clientWidth;
  canvas.height = document.documentElement.clientHeight;
}

window.onresize = makeCanvasFullPage;

makeCanvasFullPage();

var context = canvas.getContext('2d');

function centerX() {
  return canvas.width / 2;
}

function centerY() {
  return canvas.height / 2;
}

var populars = {};

var colors = ['aqua', 'yellow', 'blue', 'fuchsia', 'green',
  'lime', 'maroon', 'navy', 'olive', 'orange', 'purple', 'red',
  'silver', 'teal', 'white', 'gray'];

var balls = [];

function getPopular(hashtag) {
  var popular = populars[hashtag];

  if (!popular) {
    var num_hashtags = Object.keys(populars).length,
      color = colors[num_hashtags % colors.length];

    popular = populars[hashtag] = new Ball(color, centerX(), centerY(), hashtag);
    changePopularsDestination();
  }

  return popular;
}

function getPopulars() {
  return Object.keys(populars).map(function(key) {
    return populars[key];
  });
}

function changePopularsDestination() {
  var populars = getPopulars(),
    num = populars.length;

  populars.forEach(function (popular, index) {
    popular.destination = new Vector2D(
      centerX() + Math.cos(index / num * Math.PI*2) * centerX()/2,
      centerY() + Math.sin(index / num * Math.PI*2) * centerY()/2
    );
  });

}

function spawnBall(destination) {
  var popular = getPopular(destination);
  return new Ball(popular.color, centerX(), centerY(), popular);
}

function loop() {
  context.clearRect(0, 0, canvas.width, canvas.height);

  loopBody();

  window.requestAnimationFrame(loop);
}

function loopBody() {
  var populars = getPopulars();

  balls = balls.filter(function(ball) { return ball.move(); });
  populars.forEach(function(ball) { ball.move(); });

  balls.forEach(function(ball) { ball.draw(context); });
  populars.forEach(function(ball) { ball.draw(context); });
}

loop();
