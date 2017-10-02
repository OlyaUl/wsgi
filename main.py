#! env bin/python
# codding = utf-8
from werkzeug.wrappers import Request, Response


@Request.application
def app_dec(request):
    res = Response('hello')
    res.status = '200 OK'
    res.status_code = 400
    #res.add_cookie()
    print(request.args)
    print(request.args.getlist('a'))  # http://localhost:8000/?a=4&f=5 -> ['4']
    return res
    
    #return Response("Hello")
'''def app(environ, start_response):
    request = Request(environ)
    print(request.args)
    print(request.form)
    print(request.files)
    print(request.path)
    print(request.method)
    print(request.headers)
    response = Response('hello', mimetype='text/plain')
    return response(environ, start_response)'''

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8000, app_dec)