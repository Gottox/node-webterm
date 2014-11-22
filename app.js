var http = require('http'),
    fs = require('fs'),
    socketio = require('socket.io'),
    child_pty = require('child_pty'),
    ss = require('socket.io-stream');

process.config = require('./config.json');

var server = http.createServer()
	.on('request', function(req, res) {
		var file = null;
		console.log(req.url);
		switch(req.url) {
		case '/':
		case '/index.html':
			file = '/public/index.html';
			break;
		case '/glue.js':
			file = '/public/glue.js';
			break;
		case '/terminal.js':
			file = '/node_modules/terminal.js/dist/terminal.js';
			break;
		case '/socket.io-stream.js':
			file = '/node_modules/socket.io-stream/socket.io-stream.js';
			break;
		default:
			res.writeHead(404, {'Content-Type': 'text/plain'});
			res.end('404 Not Found');
			return;
		}
		fs.createReadStream(__dirname + file).pipe(res);
	})
	.listen(process.config.port, process.config.interface);

var io = socketio(server);

io.of('pty').on('connection', function(socket) {
	var ptys = {};

	ss(socket).on('new', function(stream, options) {
		var name = options.name;

		var pty = child_pty.spawn('/bin/sh', ['-c', process.config.login], {
			rows: options.height,
			cols: options.width,
		});
		pty.stdout.pipe(stream).pipe(pty.stdin);
		ptys[name] = pty;
	}).on('end', function(name) {
		if(name in ptys === false) return;
		ptys[name].kill();
		delete ptys[name];
	});
});

console.log('Listening on ' + process.config.interface + ':' + process.config.port);
