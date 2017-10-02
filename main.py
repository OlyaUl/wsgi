#! env bin/python
# codding = utf-8
from werkzeug.wrappers import Request, Response


def app(environ, start_response):
    request = Request(environ)
    print(request.args)
    print(request.form)
    print(request.files)
    print(request.path)
    print(request.method)
    print(request.headers)
    response = Response('hello', mimetype='text/plain')
    return response(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8000, app)