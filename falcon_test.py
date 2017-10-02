#! env bin/python
# codding = utf-8
import falcon
import json

data = []
class Resource():
    def on_get(self, req, resp):
        #resp.body = '{"message":"Hello"}'
        resp.body = json.dumps(data)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if req.content_length:
            req_data = json.loads(req.stream.read().decode())
            data.append(req_data)
        resp.status = falcon.HTTP_201
# curl -X OPTION http://localhost:8000/
#  curl  --data '{"message":"test"}'  http://localhost:8000/

app = application = falcon.API()
app.add_route('/', Resource())

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8000, app)


'''class Resource():
    def on_get(self, req, resp):
        resp.body = '{"message":"Hello"}'
        resp.status = falcon.HTTP_200

app = application = falcon.API()
app.add_route('/', Resource())

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8000, app)'''