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