from urllib import parse


def app(environ, start_response):
    data = b''
    query = parse.parse_qs(environ['QUERY_STRING'])
    for key, value in query.items():
        for item in value:
            data += '{}={}\n'.format(key, item).encode()
            
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
