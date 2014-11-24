$(document).ready(function ($) {
	var socket = io('/pty');

	$('.terminaljs').each(function() {
		this.tabindex = 0;
		var data = $(this).data();
		var text = this.textContent;

		var term = new Terminal(data);
		// Create bidirectional stream
		var stream = ss.createStream({decodeStrings: false, encoding: 'utf-8'});

		// Send stream and data to the server
		ss(socket).emit('new', stream, data);

		// Connect everything up
		stream.pipe(term).dom(this).pipe(stream);

		// Write text to terminal
		stream.write(text);
	});
});
