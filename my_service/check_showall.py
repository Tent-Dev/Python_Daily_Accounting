from bson import ObjectId

from my_service import connect_db
import datetime

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

def query_tableByDay(user_data, startdate, enddate):
    print("Load Table by Day ==> wait...")
    data_table = []
    datestart_c = datetime.datetime.strptime(startdate, '%d-%b-%Y')
    dateend_c = datetime.datetime.strptime(enddate, '%d-%b-%Y')
    db = connect_db.connectMongoDB()
    if db.transaction_list.count_documents({'username': user_data[1]}) > 0:
        get_data = db.transaction_list.find({'username': user_data[1]})

        for data in get_data:
            data_date_c = datetime.datetime.strptime(data['date'], '%d-%b-%Y')
            if datestart_c <= data_date_c <= dateend_c:
                data_table.append(data)

        print(data_table)
        print("Load Table by Day ==> success")

    else:
        print("This user not have transaction data.")

    return (data_table)