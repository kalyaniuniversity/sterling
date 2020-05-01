from flask import Flask, request, jsonify, Response
from wings.model.parsers.parser import controller
from wings.service.utils import dataframe_to_dict
import pandas as pd

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


@app.route('/api/4/', methods = ['GET'])
def method4():
    if request.method == 'GET':
        state = request.args.get('state', None)

        info = controller(4,state_code = state)

        if isinstance(info, dict):
            return jsonify(info)
        

@app.route('/api/<int:n>/', methods = ['GET'])
def methodn(n):
    info = controller(n)

    if isinstance(info, pd.DataFrame):
        info = dataframe_to_dict(info)
        return jsonify(info)


if __name__ == '__main__':
    app.run(debug=True, port=8080)