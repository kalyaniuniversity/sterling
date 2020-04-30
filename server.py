from flask import Flask, request, jsonify
from wings.model.parsers.parser import controller

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask is working' #TODO: Delete the route before deploying in the production

@app.route('/api/1/', methods = ['GET'])
def method1():
    if request.method == 'GET':
        date = request.args.get('date', None)
        state = request.args.get('state', None)

        info = controller(1, date, state)
        return jsonify(info)


@app.route('/api/2/', methods = ['GET'])
def method2():
    if request.method == 'GET':
        date = request.args.get('date', None)
        state = request.args.get('state', None)

        info = controller(2, date, state)
        return jsonify(info)


@app.route('/api/3/', methods = ['GET'])
def method3():
    if request.method == 'GET':
        state = request.args.get('state', None)

        info = controller(3,state_code = state)
        return jsonify(info)

        
@app.route('/api/<int:n>/', methods = ['GET'])
def method4(n):
    info = controller(n)
    return jsonify(info)


if __name__ == '__main__':
    app.run(debug=True, port=8080)