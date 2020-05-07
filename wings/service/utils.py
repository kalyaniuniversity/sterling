import json

def dataframe_to_dict(dataframe):

    dict_of_dataframe = json.loads(dataframe.to_json(orient='records'))

    for object in dict_of_dataframe:
        object['region'] = object.pop('STATE/UT')

    return dict_of_dataframe