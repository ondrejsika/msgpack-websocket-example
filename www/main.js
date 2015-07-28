var msgpack = require('msgpack-js-browser');


var ws = new WebSocket('ws://127.0.0.1:8888');
ws.binaryType = 'arraybuffer';
ws.onmessage = function(e){
    var payload = msgpack.decode(e.data);
    console.log(payload);
    ws.send(msgpack.encode(payload));
};
