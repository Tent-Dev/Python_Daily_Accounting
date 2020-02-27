from my_service import connect_db

def checkRegis(user):
    checkduplicate = False
    db = connect_db.connectMongoDB()
    if db.userlist.count_documents({'username': user }) != 0:
        checkduplicate = True
        print("Username is Same")
    else:
        print("Username Not Same")
    return (checkduplicate)

def insertRegister_to_Db(datainput):
    status = False
    db = connect_db.connectMongoDB()
    result = db.userlist.insert_one(datainput)
    if result.inserted_id != "":
        status = True
    return (status)

def check_inputNormal(input):
    print("Check null value ==> wait...")
    status = False
    for key,i in enumerate(input): #If have null value ==> False
        if i != "":
            print("Check null value in Index [{}] ==> ok".format(key))
            status = True
        else:
            status = False
            print("==> Found null value!")
            break
    return (status)