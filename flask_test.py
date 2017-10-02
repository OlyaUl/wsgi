from flask import Flask, render_template

app = Flask(__name__)


'''@app.route('/')
def index():
    return 'Hello'
'''


@app.route('/')
@app.route('/<hash>', methods=['GET'])
def hash(hash=0):
    return render_template('hash.html', hash=hash, params=range(5))  #'hash = %s' % hash

if __name__ == '__main__':
    app.run()  # working in 5000 port  http://localhost:5000/
