import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="library"
    )
mycursor = mydb.cursor()
options = ('log in', 'create')
x = input('''would you like to log in or create a password? 
         please type 'log in' or 'create':''')
if x == options[1]:
    user = input('choose a user name:')
    pas = input('choose a password:')
    email = input('enter your email:')
      #INSERT INTO students TABLE AND COMMIT DATA##
    sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    val = (user, email, pas)
    mycursor.execute(sql, val)
elif x == options[0]:
    loguser = input('please enter your username:')
    logpas = input('please enter your password:')
    SELECT * FROM library.users WHERE username = 'loguser' AND password = 'logpas'
    myresult = mycursor.fetchall()
    trys = 0
    while trys != 3:
        if logpas not in myresult:
            guess = input('''you have entered an incorect password
            please enter the corect password:''')
            trys = trys + 1
        else:
            print(email)
    if trys == 3:
        print('you have entered an incorect password too many times')