from bson import ObjectId

from my_service import connect_db
import datetime

def query_table(user_data,date_select):
    print("Load Table by Day ==> wait...")
    data_table = []
    date_select_c = datetime.datetime.strptime(date_select, '%d-%b-%Y')
    db = connect_db.connectMongoDB()
    if db.transaction_list.count_documents({'username': user_data[1]}) > 0:
        get_data = db.transaction_list.find({'username': user_data[1]})

        for data in get_data:

            data_date_c = datetime.datetime.strptime(data['date'], '%d-%b-%Y')
            if data_date_c == date_select_c:
                data_table.append(data)

        print(data_table)
        print("Load Table by Day ==> success")

    else:
        print("This user not have transaction data.")

    return (data_table)

def checkEditLedger(datainput,user_data,old_data):
    print("Editing data ==> wait...")
    print("Old data ==> {}".format(old_data))
    print("Old data ==> {}".format(datainput))
    db = connect_db.connectMongoDB()
    check_added = db.transaction_list.update_one({'_id': old_data['_id']} , {'$set': datainput})
    if(check_added.matched_count > 0):
        print("Editing data ==> success")
        check_added_bool = True
    else:
        print("Editing data ==> Error")
        check_added_bool = False

    return (check_added_bool)

def checkDeleteLedger(id):
    print('Delete transaction id : {}'.format(id))
    print('Delete transaction ==> wait...')
    db = connect_db.connectMongoDB()
    check_delete = db.transaction_list.delete_one({'_id': ObjectId(id)})
    print(check_delete)
    print('Delete transaction ==> success')