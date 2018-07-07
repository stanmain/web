# def app(environ, start_response):
#     """Simplest possible application object"""
#     data = b'Hello, World!\n'
#     status = '200 OK'
#     response_headers = [
#         ('Content-type', 'text/plain'),
#         ('Content-Length', str(len(data)))
#     ]
#     start_response(status, response_headers)
#     return iter([data])

def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
