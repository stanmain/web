# from urllib import parse


def app(environ, start_response):
    data = []
    ll = 0
    # query = parse.parse_qs(environ['QUERY_STRING'])
    query = environ['QUERY_STRING'].replace('&', '\n')

    # for key, value in query.items():
    #     for item in value:
    #         dd = '{}={}\n'.format(key, item).encode()
    #         data.append(dd)
    #         ll += len(dd)
    data = query.encode()
    print(len(data))
    print(data)
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
