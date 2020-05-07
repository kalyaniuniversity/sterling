import json

def df_to_jsonObject(df):

    df_json_string = json.loads(df.to_json(orient='records'))
    
    data = dict()

    for object in df_json_string:
        state = object['STATE/UT']
        del object['STATE/UT']
        data[state] = object

    return data