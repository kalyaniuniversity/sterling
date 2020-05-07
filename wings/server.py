from flask import Flask, jsonify
from model.parsers.parser import controller
from service.utils import dataframe_to_dict
import pandas as pd

app = Flask(__name__)

@app.route('/get/cummulative/<string:date>/<string:state>/', methods = ['GET'])
def cummulative(date, state):
    info = controller(1, date, state)
    return jsonify(info)


@app.route('/get/cummulative/datewise/<string:date>/<string:state>/', methods = ['GET'])
def cummulative_datewise(date, state):
    info = controller(2, date, state)
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