import json

def dataframe_to_dict(dataframe):
    """Converts a dataframe to an object of python dictionary class

    Arguments:
        dataframe {pandas.Dataframe} -- object of pandas.Dataframe class

    Returns:
        dictionary -- object of python dict class
    """

    dict_of_dataframe = json.loads(dataframe.to_json(orient='records'))

    for object in dict_of_dataframe:
        object['Region'] = object.pop('STATE/UT')

    return dict_of_dataframe