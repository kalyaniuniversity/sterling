import requests
from wings.model.parsers import model as m

dataset = m.initialize()

unique_dates = list()

raw_data = requests.get('https://api.covid19india.org/v2/state_district_wise.json')
raw_json = raw_data.json()

for state_dict in range(len(raw_json)):
    
    for i in range(len(dataset)):

        if raw_json[state_dict]['state'] == dataset[i]['name']:

            dataset[i]['districts'] = dict()

            for district_dict in range(len(raw_json[state_dict]['districtData'])):

                district_name = raw_json[state_dict]['districtData'][district_dict]['district']
                dataset[i]['districts'][district_name] = dict()
                dataset[i]['districts'][district_name]['confirmed'] = raw_json[state_dict]['districtData'][district_dict]['confirmed']

def total_count(state_code):

        for states in dataset:

                total = 0
                if state_code == states['code']:
                        if 'districts' in states:
                                for district in states['districts']:
                                        confirm =  states['districts'][district]['confirmed']
                                        total = total + confirm
                                return total
                        else:
                                return total
                
                else:
                        continue
