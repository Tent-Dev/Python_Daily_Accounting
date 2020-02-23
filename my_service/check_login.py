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
    else:
        datalogin.append("FAIL")
    return (datalogin)