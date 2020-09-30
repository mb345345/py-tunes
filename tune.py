# a note on tiny db
# to install it first run from the command line: pip install tinydb

# init
from tinydb import TinyDB, Query
db = TinyDB('db.json')
db.truncate()
user_table = db.table('user_table')
user_query = Query()

print("welcome to tune manager")

# log in
loggedIn = False
while loggedIn == False:

    # log in or register?
    print("log in or register")
    decision = input()

    if decision[0:3].lower() == "log":
            
        # log in
        print("please log in")
        print("enter your email:")
        email = input()
        print("enter your password:")
        password = input()

        # get user from db
        this_user = user_table.search(user_query.email == email and user_query.password == password)

        if len(this_user) == 1:

            print("you logged in :)")
            loggedIn = True
        
        else:

            print("sorry, log in failed")
            print("do you need to register?")
    
    else:

        # register
        print("please register")
        print("enter your email:")
        email = input()
        print("enter your password:")
        password = input()

        # get user from db
        this_user = user_table.search(user_query.email == email)
        if len(this_user) >= 1:

            print("sorry, this user is already registered")
            print("do you need to log in?")

            continue

        # insert user into db
        user_table.insert({'email': email, 'password': password})
        
        # registered
        print("thank you for registering :)")
        loggedIn = True

        







