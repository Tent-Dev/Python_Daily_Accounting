from my_service import connect_db
import datetime

def query_table(user_data,date_select):
    print("Load Table by Day ==> wait...")
    data_table = []
    date_select_c = datetime.datetime.strptime(date_select, '%d-%b-%Y')
    db = connect_db.connectMongoDB()
    if db.userlist.count_documents({'username': user_data[1]}) == 1:
        get_data = db.userlist.find({'username': user_data[1]})

        for data in get_data:
            transaction_data = data
        if 'date_transaction' not in transaction_data:
            print("This user not have transaction data.")
        else:
            for transaction in transaction_data['date_transaction']:
                data_date_c = datetime.datetime.strptime(transaction['date'], '%d-%b-%Y')
                if data_date_c == date_select_c:
                    data_table.append(transaction)
            print(data_table)
            print("Load Table by Day ==> success")

    else:
        data_table.append("FAIL")
        print("Load Table by Day ==> Error")
    return (data_table)

def checkEditLedger(datainput,user_data,old_data):
    print("Editing data ==> wait...")
    db = connect_db.connectMongoDB()
    check_added = db.userlist.update_one({'username': user_data[1],
                                          'date_transaction.date': old_data['date'],
                                          'desc': old_data['desc']
                                          } , {'$set': {'date_transaction': datainput}})
    if(check_added.matched_count > 0):
        print("Editing data ==> success")
        check_added_bool = True
    else:
        print("Editing data ==> Error")
        check_added_bool = False
    return (check_added_bool)