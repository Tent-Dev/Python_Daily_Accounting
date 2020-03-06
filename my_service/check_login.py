import datetime

from my_service import connect_db

def checkLogin(datainput):
    datalogin = []
    db = connect_db.connectMongoDB()
    if db.userlist.count_documents({'username': datainput['username'] ,'password' : datainput['password']}) == 1:
        datalogin.append("PASS")
        get_data = db.userlist.find({'username': datainput['username']})
        for data in get_data:
            datalogin.append(data['username'])
            datalogin.append(data['Fname'])
            datalogin.append(data['Lname'])
        print('Info ==> {}'.format(datalogin))
        print('-'*30)
    else:
        datalogin.append("FAIL")
    return (datalogin)

def query_data(user_data):
    print("load user data {} ==> wait...".format(user_data[1]))
    data_transaction = []
    income_sum = 0
    spend_sum = 0
    spend_sum_monthLimit = 0
    now = datetime.datetime.today().strftime('%b-%Y')
    day_c = datetime.datetime.strptime(now, '%b-%Y').strftime('%b-%Y')

    db = connect_db.connectMongoDB()
    if db.transaction_list.count_documents({'username': user_data[1]}) > 0:
        get_data = db.transaction_list.find({'username': user_data[1]})

        for data in get_data:
            print(data)
            transaction_data = data

            income_sum = income_sum+transaction_data['income']
            spend_sum = spend_sum + transaction_data['spend']

            day_data_c = datetime.datetime.strptime(data['date'], '%d-%b-%Y').strftime('%b-%Y')

            if day_c == day_data_c:
                spend_sum_monthLimit = spend_sum_monthLimit+transaction_data['spend']

        get_Userdata = db.userlist.find({'username': user_data[1]})
        for data in get_Userdata:
            user_data_result = data

        print("Sum income ==> {} Bath.".format(income_sum))
        print("Sum spend ==> {} Bath.".format(spend_sum))
        print("Sum spend in this month ==> {} Bath.".format(spend_sum_monthLimit))
        print("load user data ==> success")
        print('-' * 30)
        if 'limit_value_temp' in user_data_result:
            data_transaction = {'income_sum': income_sum,
                                'spend_sum': spend_sum,
                                'limit_value': user_data_result['limit_value_temp'][-1]['limit_value'],
                                'spend_limit_month_sum': spend_sum_monthLimit}
        else:
            data_transaction = {'income_sum': income_sum,
                                'spend_sum': spend_sum,
                                'limit_value': 0,
                                'spend_limit_month_sum': spend_sum_monthLimit}

    else:
        print("This user not have transaction data.")
        data_transaction = {'income_sum': income_sum,
                            'spend_sum': spend_sum,
                            'limit_value': 0,
                            'spend_limit_month_sum': 0}

    return (data_transaction)

def query_table(user_data):

    print("Load Table ==> wait...")
    data_table = []
    db = connect_db.connectMongoDB()
    if db.transaction_list.count_documents({'username': user_data[1]}) > 0:
        get_data = db.transaction_list.find({'username': user_data[1]})

        for data in get_data:
            data_table.append(data)

        print(data_table)
        print("Load Table ==> success")

    else:
        print("This user not have transaction data.")

    return (data_table)