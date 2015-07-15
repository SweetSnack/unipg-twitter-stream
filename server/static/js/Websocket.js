(function() {
  //  setup websocket with callbacks
  var ws = new WebSocket('ws://localhost:8080/ws');

  ws.onopen = function() {
    console.log('CONNECTED');
  };
  ws.onclose = function() {
    console.log('DISCONNECTED');
  };
  ws.onmessage = function(event) {
    balls.push(spawnBall(event.data));
  };
})();