import datetime

from my_service import connect_db

def checkAddlimitValue(datainput, user_data):
    print(datainput)
    print("Save limit value ==> wait...")
    db = connect_db.connectMongoDB()
    check_added = db.userlist.update_one({'username': user_data[1]}, {'$push': {'limit_value_temp': datainput}})
    if(check_added.matched_count > 0):
        print("Save limit value ==> success")
        check_added_bool = True
    else:
        print("Save limit value ==> Error")
        check_added_bool = False
    return (check_added_bool)

def query_limitValue(user_data):
    print("load limit value ==> wait...")
    data_limitValue = []
    db = connect_db.connectMongoDB()
    if db.userlist.count_documents({'username': user_data[1]}) == 1:
        data_limitValue.append("PASS")
        get_data = db.userlist.find({'username': user_data[1]})

        for data in get_data:
            all_limitValue = data

        if 'limit_value_temp' not in all_limitValue:
            print("This user not have limit value data.")
            data_limitValue.append(0)
        else:
            temp_value = all_limitValue['limit_value_temp'][-1]
            data_limitValue.append(temp_value['limit_value'])

        print('Info ==> {}'.format(data_limitValue))
        print("load limit value ==> Success")

    else:
        data_limitValue.append("FAIL")
        print("load limit value ==> Error")
    return (data_limitValue)

def query_data(user_data, day):
    print("load user data {} | {} ==> wait...".format(day,user_data[1]))
    day_c = datetime.datetime.strptime(day, '%b-%Y').strftime('%b-%Y')
    data_transaction = []
    income_sum = 0
    spend_sum = 0
    db = connect_db.connectMongoDB()
    if db.transaction_list.count_documents({'username': user_data[1]}) > 0:
        get_data = db.transaction_list.find({'username': user_data[1]})

        for data in get_data:
            day_data_c = datetime.datetime.strptime(data['date'], '%d-%b-%Y').strftime('%b-%Y')
            print('{} | {}'.format(day_c, day_data_c))
            if day_c == day_data_c:
                print(data)
                transaction_data = data

                income_sum = income_sum+transaction_data['income']
                spend_sum = spend_sum + transaction_data['spend']

        get_Userdata = db.userlist.find({'username': user_data[1]})
        for data in get_Userdata:
            user_data_result = data

        print("Sum income ==> {} Bath.".format(income_sum))
        print("Sum spend ==> {} Bath.".format(spend_sum))
        print("load user data ==> success")
        print('-' * 30)
        if 'limit_value_temp' in user_data_result:
            data_transaction = {'income_sum': income_sum,
                                'spend_sum': spend_sum,
                                'limit_value': user_data_result['limit_value_temp'][-1]['limit_value']}
        else:
            data_transaction = {'income_sum': income_sum,
                                'spend_sum': spend_sum,
                                'limit_value': 0}

    else:
        print("This user not have transaction data.")
        data_transaction = {'income_sum': income_sum, 'spend_sum': spend_sum, 'limit_value': 0}

    return (data_transaction)

def query_alllimit(user_data):
    print("load limit history table ==> wait...")
    data_limitValue = []
    data_transaction = 0
    db = connect_db.connectMongoDB()
    if db.userlist.count_documents({'username': user_data[1]}) == 1:
        get_data = db.userlist.find({'username': user_data[1]})
        get_data_transaction = db.transaction_list.find({'username': user_data[1]})
        for data in get_data:

            for date_query in data['limit_value_temp']:
                print('Limit value {} ==> {}'.format(date_query['date_create'], date_query['limit_value']))
                dateend_c = datetime.datetime.strptime(date_query['date_create'], '%d-%b-%Y').strftime('%b-%Y')
                for query_transaction in get_data_transaction:
                    datestart_c = datetime.datetime.strptime(query_transaction['date'], '%d-%b-%Y').strftime('%b-%Y')
                    if datestart_c == dateend_c:
                        data_transaction = data_transaction+query_transaction['spend']
                used_value = date_query['limit_value'] - data_transaction
                print('used in {} ==> {}'.format(date_query['date_create'], used_value))
                result = {'date_create': date_query['date_create'],'limit_value': date_query['limit_value'],'used': used_value}
                data_limitValue.append(result)
        print("load limit history table ==> Success")
    return (data_limitValue)