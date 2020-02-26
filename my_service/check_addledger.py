from my_service import connect_db

def checkAddLedger(datainput,user_data):
    print("adding new data ==> wait...")
    db = connect_db.connectMongoDB()
    check_added = db.userlist.update_one({'username': user_data[1]}, {'$push': {'date_transaction': datainput}})
    if(check_added.matched_count > 0):
        print("adding new data ==> success")
        check_added_bool = True
    else:
        print("adding new data ==> Error")
        check_added_bool = False
    return (check_added_bool)