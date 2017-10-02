#! env bin/python
# codding = utf-8
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response

map_rule = Map([
    Rule('/', endpoint='index'),
    Rule('/<hash>', endpoint='hash'),
])


def app(environ, start_response):
    urls = map_rule.bind_to_environ(environ)
    try:
        endpoint, args = urls.match()
    except Exception:
        return [b'Error']
    print(endpoint)
    print(args)
    resp = Response('OK')
    return resp(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8000, app)
