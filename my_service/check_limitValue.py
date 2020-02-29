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