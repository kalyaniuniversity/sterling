from model.parsers import states_daily_parser as sdp
from model.parsers import state_district_wise_parser as sdwp
from model.parsers import model as m

def controller(choice, date_to_fetch = None, state_code = None):

    while choice != 16:

        if choice == 1:

            if state_code.islower() == False:
                state_code = state_code.lower()
            else:
                state_code = state_code

            if sdp.state_code_validate(state_code) != 0:

                if sdp.date_validate(date_to_fetch) != 0:

                    if sdp.cumulative_data(date_to_fetch, state_code) == 0:
                        return 0
                    else:
                        return sdp.cumulative_data(date_to_fetch, state_code)
                else:
                    
                    continue
            else:
                if sdp.date_validate(date_to_fetch) == 0:
                    continue
                else: 
                    continue
            
        elif choice == 2:

            if state_code.islower() == False:
                state_code = state_code.lower()

            else:
                state_code = state_code

            if sdp.state_code_validate(state_code) != 0: 
                if sdp.date_validate(date_to_fetch) != 0:
                    return sdp.cumulative_series_datewise_data(date_to_fetch, state_code)

                else:
                    continue
            else:
                if sdp.date_validate(date_to_fetch) == 0:
                    continue

                else: 
                    continue

        elif choice == 3:

            if state_code.islower() == False:
                state_code = state_code.lower()

            else:
                state_code = state_code

            if sdp.state_code_validate(state_code) != 0: 
                return sdp.cumulative_last_3_days(state_code)

            else:
                continue
        
        elif choice == 4:  
            return sdp.cumulative_last_3_days_all_states(choice)
    
        elif choice == 5:
            return sdp.make_data_frame()

        elif choice == 6:
            return sdp.cumulative_last_3_days_confirmed_dataframe(choice)

        elif choice == 7:
            return sdp.cumulative_last_3_days_recovered_dataframe(choice)

        elif choice == 8:
            return sdp.cumulative_last_3_days_deceased_dataframe(choice)

        elif choice == 9:
            return sdp.all_data_confirmed()

        elif choice == 10:
            return sdp.all_data_recovered()

        elif choice == 11:
            return sdp.all_data_deceased()

        elif choice == 12:
            return sdp.cumulative_all_data_confirmed()

        elif choice == 13:
            return sdp.cumulative_all_data_recovered()

        elif choice == 14:
            return sdp.cumulative_all_data_deceased()

        else:
            print('Invalid choice, please choose again\n')

    print("\nProgram has quit")

