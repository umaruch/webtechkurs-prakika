def app(environ, start_response):
	data = bytes(environ.get('QUERY_STRING').replace('&', '\n'), 'UTF-8')
	start_response("200 OK", [
	('Content-Type', 'text/plain'),
	('Content-Length', str(len(data)))
	])
	return iter([data])
