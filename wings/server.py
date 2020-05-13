from flask import Flask, jsonify
from model.parsers.parser import controller
from service.utils import dataframe_to_dict
import pandas as pd

app = Flask(__name__)


@app.route('/get/cummulative/<string:date>/<string:state>/', methods=['GET'])
def cummulative(date, state):
    info = controller(1, date, state)
    return jsonify(info)


@app.route('/get/cummulative/datewise/<string:date>/<string:state>/', methods=['GET'])
def cummulative_datewise(date, state):
    info = controller(2, date, state)
    return jsonify(info)


@app.route('/get/cummulative/last-3-days/<string:state>/', methods=['GET'])
def cummulative_last_3_days(state):
    info = controller(3, state_code=state)
    return jsonify(info)


@app.route('/get/cummulative/last-3-days/all-states/', methods=['GET'])
def cummulative_last_3_days_all():
    info = controller(4)
    if isinstance(info, dict):
        return jsonify(info)


@app.route('/get/cummulative/all-states/', methods=['GET'])
def cummulative_all():
    info = controller(5)

    if isinstance(info, pd.DataFrame):
        info = dataframe_to_dict(info)
        return jsonify(info)


@app.route('/get/cummulative/confirmed/last-3-days/all-states/', methods=['GET'])
def cummulative_confirmed_last_3_days_all():
    info = controller(6)

    if isinstance(info, pd.DataFrame):
        info = dataframe_to_dict(info)
        return jsonify(info)


@app.route('/get/cummulative/recovered/last-3-days/all-states/', methods=['GET'])
def cummulative_recovered_last_3_days_all():
    info = controller(7)

    if isinstance(info, pd.DataFrame):
        info = dataframe_to_dict(info)
        return jsonify(info)


@app.route('/get/cummulative/deceased/last-3-days/all-states/', methods=['GET'])
def cummulative_deceased_last_3_days_all():
    info = controller(8)

    if isinstance(info, pd.DataFrame):
        info = dataframe_to_dict(info)
        return jsonify(info)


@app.route('/get/datewise/confirmed/all-states/', methods=['GET'])
def datewise_confirmed_all():
    info = controller(9)

    if isinstance(info, pd.DataFrame):
        info = dataframe_to_dict(info)
        return jsonify(info)


@app.route('/get/datewise/recovered/all-states/', methods=['GET'])
def datewise_recovered_all():
    info = controller(10)

    if isinstance(info, pd.DataFrame):
        info = dataframe_to_dict(info)
        return jsonify(info)


@app.route('/get/datewise/deceased/all-states/', methods=['GET'])
def datewise_deceased_all():
    info = controller(11)

    if isinstance(info, pd.DataFrame):
        info = dataframe_to_dict(info)
        return jsonify(info)


@app.route('/get/cummulative/confirmed/all-states/', methods=['GET'])
def cummulative_confirmed_all():
    info = controller(12)

    if isinstance(info, pd.DataFrame):
        info = dataframe_to_dict(info)
        return jsonify(info)


@app.route('/get/cummulative/recovered/all-states/', methods=['GET'])
def cummulative_recovered_all():
    info = controller(13)

    if isinstance(info, pd.DataFrame):
        info = dataframe_to_dict(info)
        return jsonify(info)


@app.route('/get/cummulative/deceased/all-states/', methods=['GET'])
def cummulative_deceased_all():
    info = controller(14)

    if isinstance(info, pd.DataFrame):
        info = dataframe_to_dict(info)
        return jsonify(info)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
