#! env bin/python
# codding = utf-8
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response


def index(request):
    return Response('index page')


def hash(request, hash):
    return Response('hash = %s' % hash)

map_rule = Map([
    Rule('/', endpoint='index'),
    Rule('/<hash>', endpoint='hash'),
])

views = {
    'index': index,
    'hash': hash
}

def app(environ, start_response):
    urls = map_rule.bind_to_environ(environ)
    try:
        endpoint, args = urls.match()
    except Exception:
        start_response('404 Not Found')
        return [b'rule not found']

    resp = views[endpoint](Request(environ), **args)
    return resp(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8000, app)
