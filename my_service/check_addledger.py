from my_service import connect_db

def checkAddLedger(datainput):

    print("adding new data ==> wait...")
    db = connect_db.connectMongoDB()
    check_added = db.transaction_list.insert_one(datainput)
    if(check_added != ""):
        print("adding new data ==> success")
        check_added_bool = True
    else:
        print("adding new data ==> Error")
        check_added_bool = False

    return (check_added_bool)