import requests
from wings.model.parsers import model as m
import pandas as pd
import datetime

dataset = m.initialize()
unique_dates = list()

raw_data = requests.get('https://api.covid19india.org/states_daily.json')
raw_json = raw_data.json()

for item in raw_json['states_daily']:

    if item['date'] not in unique_dates:
      unique_dates.append(item['date'])

for date in unique_dates:

    for item in raw_json['states_daily']:

        if date == item['date']:

            for state in dataset:

                if date not in state:
                    state[date] = dict()

                state[date][item['status']] = item[state['code']]

def date_validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%b-%y')
    except ValueError:
        print("Incorrect date format, should be dd-Mmm-yy")
        return 0

def state_code_validate(state_code):

    unique_states = list()
    for item in dataset:
        unique_states.append(item['code'])
    
    if state_code in unique_states:
        return 1
    else:
        print('Please enter a valid state code')
        return 0

def needs_patch(date_to_fetch, state_code):

    if (date_to_fetch == '26-Mar-20' and state_code == 'ap') or (date_to_fetch == '16-Mar-20' and state_code == 'mp'):
        return True
    return False

def apply_patch(date_to_fetch, state_code):

    if date_to_fetch == '26-Mar-20' and state_code == 'ap':
        return {'Confirmed': '1', 'Recovered': '0', 'Deceased': '0'}
    if date_to_fetch == '16-Mar-20' and state_code == 'mp':
        return {'Confirmed': '0', 'Recovered': '0', 'Deceased': '0'}

def fetch_by_date_and_code(date_to_fetch, state_code):

    if(needs_patch(date_to_fetch, state_code)):
        return apply_patch(date_to_fetch, state_code)

    if date_to_fetch == '26-Mar-20' and state_code == 'ap':
        return {'Confirmed': '1', 'Recovered': '0', 'Deceased': '0'}
    if date_to_fetch == '16-Mar-20' and state_code == 'mp':
        return {'Confirmed': '0', 'Recovered': '0', 'Deceased': '0'}


    if date_to_fetch in unique_dates:

        for state in dataset:

            if state['code'] == state_code:

                if date_to_fetch in state:
                    return state[date_to_fetch]
    else :
        print('date does not exist')

def cumulative_datewise_data(date_to_fetch, state_code):

    should_stop = False

    for unique_date in unique_dates:

        if unique_date == date_to_fetch:
            should_stop = True
        
        print(unique_date, fetch_by_date_and_code(unique_date, state_code))

        if should_stop:
            break

def cumulative_data(date_to_fetch, state_code):

    should_stop = False
    cumulative_dict = dict()
    if date_to_fetch in unique_dates:
            for unique_date in unique_dates:

                if unique_date == date_to_fetch:
                    should_stop = True

                returned_dict = fetch_by_date_and_code(unique_date, state_code)
                
                for key in returned_dict:

                    if key in cumulative_dict:
                        cumulative_dict[key] += int(returned_dict[key])
                    else:
                        cumulative_dict[key] = int(returned_dict[key])

                if should_stop:
                    break
            return cumulative_dict

    else:
            return 0

    


def cumulative_series_datewise_data(date_to_fetch, state_code):

    should_stop = False
    cumulative_series_datewise_dict = dict()

    if date_to_fetch in unique_dates:

        for unique_date in unique_dates:

            if unique_date == date_to_fetch:
                should_stop = True
        
            cumulative_series_datewise_dict[unique_date] = cumulative_data(unique_date, state_code)

            if should_stop:
                break

        return cumulative_series_datewise_dict
    else:
        print('date does not exist')

def cumulative_last_3_days(state_code, should_print = False):

    resultset = dict()

    for unique_date in unique_dates[-3:]:
        resultset[unique_date] = cumulative_data(unique_date, state_code)
        if should_print:
            print(unique_date, cumulative_data(unique_date, state_code))

    return resultset



def view_cumulative_last_3_days_all_states(resultset):

    global unique_dates

    for unique_date in unique_dates[-3:]:

        print('\n', unique_date, '\n')
        for state in resultset:

            if unique_date in resultset[state]:
                
                print(state, '\t\t', end = ' ')
                print('C:', resultset[state][unique_date]['Confirmed'], ' || R:', resultset[state][unique_date]['Recovered'], ' || D:', resultset[state][unique_date]['Deceased'])

def cumulative_last_3_days_all_states(choice):

    resultset = dict()

    for state in dataset:
        resultset[state['name']] = cumulative_last_3_days(state['code'], False)
    

    return resultset

    


def total_count(state_code):

    cumulative_dict = dict()

    for unique_date in unique_dates:

        returned_dict = fetch_by_date_and_code(unique_date, state_code)
        
        for key in returned_dict:
            if key in cumulative_dict:
                cumulative_dict[key] += int(returned_dict[key])
            else:
                cumulative_dict[key] = int(returned_dict[key])
    
    return cumulative_dict
def make_data_frame():

        unique_states =  list()
        confirmed_list = list()
        recovery_list = list()
        deceased_list = list()

        for state in dataset[:-1]:
                if state['name'] not in unique_states:
                        unique_states.append(state['name'])

        for state in dataset[:-1]:

                status = total_count(state['code'])
                confirmed_list.append(status['Confirmed'])
                recovery_list.append(status['Recovered'])
                deceased_list.append(status['Deceased'])

        data = {'STATE/UT':unique_states, 'Confirmed':confirmed_list, 'Recovered':recovery_list, 'Deceased':deceased_list}
        df = pd.DataFrame(data, columns = ['STATE/UT', 'Confirmed', 'Recovered', 'Deceased'])
        return df

def cumulative_last_3_days_confirmed_dataframe(choice):

    unique_states =  list()
    dates = dict()
    unique_dates = list()
    date_dict = dict()

    for state in dataset:
        if state['name'] not in unique_states:
            unique_states.append(state['name'])
    resultset = cumulative_last_3_days_all_states(choice)
    for state in resultset:
      
        for date in resultset[state]:
          if date not in date_dict:
            date_dict[date] = list()
            dates[date] = date_dict[date]
            unique_dates.append(date)
    
    for state in resultset:
        for date in resultset[state]:
            dates[date].append(resultset[state][date]['Confirmed'])

    data = {'STATE/UT':unique_states, unique_dates[0]:dates[unique_dates[0]], unique_dates[1]:dates[unique_dates[1]], unique_dates[2]:dates[unique_dates[2]]}
    df = pd.DataFrame(data)
    return df

def cumulative_last_3_days_recovered_dataframe(choice):

    unique_states =  list()
    dates = dict()
    unique_dates = list()
    date_dict = dict()

    for state in dataset:

        if state['name'] not in unique_states:
            unique_states.append(state['name'])

    resultset = cumulative_last_3_days_all_states(choice)

    for state in resultset:
      
        for date in resultset[state]:

          if date not in date_dict:

            date_dict[date] = list()
            dates[date] = date_dict[date]
            unique_dates.append(date)
    
    for state in resultset:

        for date in resultset[state]:
            dates[date].append(resultset[state][date]['Recovered'])
    
    data = {'STATE/UT':unique_states, unique_dates[0]:dates[unique_dates[0]], unique_dates[1]:dates[unique_dates[1]], unique_dates[2]:dates[unique_dates[2]]}
    df = pd.DataFrame(data)
    return df


def cumulative_last_3_days_deceased_dataframe(choice):

    unique_states =  list()
    dates = dict()
    unique_dates = list()
    date_dict = dict()

    for state in dataset:

        if state['name'] not in unique_states:
            unique_states.append(state['name'])

    resultset = cumulative_last_3_days_all_states(choice)

    for state in resultset:
      
        for date in resultset[state]:
          if date not in date_dict:
            date_dict[date] = list()
            dates[date] = date_dict[date]
            unique_dates.append(date)
    
    for state in resultset:

        for date in resultset[state]:
            dates[date].append(resultset[state][date]['Deceased'])

    data = {'STATE/UT':unique_states, unique_dates[0]:dates[unique_dates[0]], unique_dates[1]:dates[unique_dates[1]], unique_dates[2]:dates[unique_dates[2]]}
    df = pd.DataFrame(data)
    return df


def all_data_confirmed():

    unique_states =  list()
    dates = dict()
    unique_dates = list()
    date_dict = dict()

    for state in dataset:

        if state['name'] not in unique_states:
            unique_states.append(state['name'])

    for state in dataset:

        for date in state:
          if date != 'code' and date != 'name':
            date_dict[date] = list()
            dates[date] = date_dict[date]
            unique_dates.append(date)

    for state in dataset:

        for date in state:
          if date != 'code' and date != 'name':
            dates[date].append(state[date]['Confirmed'])
 
    data = {'STATE/UT':unique_states}
    for date in dates:
        data[date] = dates[date]
   
    df = pd.DataFrame(data)
    return df

def all_data_recovered():

    unique_states =  list()
    dates = dict()
    unique_dates = list()
    date_dict = dict()

    for state in dataset:

        if state['name'] not in unique_states:
            unique_states.append(state['name'])

    for state in dataset:

        for date in state:
          if date != 'code' and date != 'name':
            date_dict[date] = list()
            dates[date] = date_dict[date]
            unique_dates.append(date)

    for state in dataset:

        for date in state:
          if date != 'code' and date != 'name':
            dates[date].append(state[date]['Recovered'])
 
    data = {'STATE/UT':unique_states}

    for date in dates:
        data[date] = dates[date]
   
    df = pd.DataFrame(data)
    return df

def all_data_deceased():

    unique_states =  list()
    dates = dict()
    unique_dates = list()
    date_dict = dict()

    for state in dataset:

        if state['name'] not in unique_states:
            unique_states.append(state['name'])

    for state in dataset:

        for date in state:
          if date != 'code' and date != 'name':
            date_dict[date] = list()
            dates[date] = date_dict[date]
            unique_dates.append(date)

    for state in dataset:

        for date in state:
          if date != 'code' and date != 'name':
            dates[date].append(state[date]['Deceased'])
 
    data = {'STATE/UT':unique_states}
    for date in dates:
        data[date] = dates[date]
   
    df = pd.DataFrame(data)
    return df

def cumulative_all_data_confirmed():

    unique_states =  list()
    dates = dict()
    unique_dates = list()
    date_dict = dict()

    for state in dataset:

        if state['name'] not in unique_states:
            unique_states.append(state['name'])

    for state in dataset:

        for date in state:
          if date != 'code' and date != 'name':
            date_dict[date] = list()
            dates[date] = date_dict[date]
            unique_dates.append(date)

    for state in dataset:

        for date in state:
          if date != 'code' and date != 'name':
            cumulative_dict = cumulative_data(date, state['code'])
            dates[date].append(cumulative_dict['Confirmed'])
 
    data = {'STATE/UT':unique_states}
    for date in dates:
        data[date] = dates[date]
   
    df = pd.DataFrame(data)
    return df

def cumulative_all_data_recovered():

    unique_states =  list()
    dates = dict()
    unique_dates = list()
    date_dict = dict()

    for state in dataset:

        if state['name'] not in unique_states:
            unique_states.append(state['name'])

    for state in dataset:

        for date in state:
          if date != 'code' and date != 'name':
            date_dict[date] = list()
            dates[date] = date_dict[date]
            unique_dates.append(date)

    for state in dataset:

        for date in state:

          if date != 'code' and date != 'name':
            cumulative_dict = cumulative_data(date, state['code'])
            dates[date].append(cumulative_dict['Recovered'])
 
    data = {'STATE/UT':unique_states}
    for date in dates:
        data[date] = dates[date]
   
    df = pd.DataFrame(data)
    return df

def cumulative_all_data_deceased():

    unique_states =  list()
    dates = dict()
    unique_dates = list()
    date_dict = dict()

    for state in dataset:

        if state['name'] not in unique_states:
            unique_states.append(state['name'])

    for state in dataset:

        for date in state:

          if date != 'code' and date != 'name':
            date_dict[date] = list()
            dates[date] = date_dict[date]
            unique_dates.append(date)

    for state in dataset:

        for date in state:

          if date != 'code' and date != 'name':
            cumulative_dict = cumulative_data(date, state['code'])
            dates[date].append(cumulative_dict['Deceased'])
 
    data = {'STATE/UT':unique_states}

    for date in dates:
        data[date] = dates[date]
   
    df = pd.DataFrame(data)
    return df





