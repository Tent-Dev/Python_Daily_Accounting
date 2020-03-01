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
    print("load user data ==> wait...")
    data_transaction = []
    income_sum = 0
    spend_sum = 0
    db = connect_db.connectMongoDB()
    if db.userlist.count_documents({'username': user_data[1]}) == 1:
        get_data = db.userlist.find({'username': user_data[1]})

        for data in get_data:
            transaction_data = data
        if 'date_transaction' not in transaction_data:
            print("This user not have transaction data.")
        else:
            for transaction in transaction_data['date_transaction']:
                income_sum = income_sum+transaction['income']
                spend_sum = spend_sum + transaction['spend']
            print("Sum income ==> {} Bath.".format(income_sum))
            print("Sum spend ==> {} Bath.".format(spend_sum))
            print("load user data ==> success")
            print('-' * 30)

        data_transaction = {'income_sum': income_sum, 'spend_sum':spend_sum}


    else:
        data_transaction.append("FAIL")
        print("load limit value ==> Error")
    return (data_transaction)

def query_table(user_data):
    print("Load Table ==> wait...")
    data_table = []
    db = connect_db.connectMongoDB()
    if db.userlist.count_documents({'username': user_data[1]}) == 1:
        get_data = db.userlist.find({'username': user_data[1]})

        for data in get_data:
            transaction_data = data
        if 'date_transaction' not in transaction_data:
            print("This user not have transaction data.")
        else:
            for transaction in transaction_data['date_transaction']:
                data_table.append(transaction)
            print(data_table)
            print("Load Table ==> success")

    else:
        data_table.append("FAIL")
        print("Load Table ==> Error")
    return (data_table)