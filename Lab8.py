import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode
import time

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'library',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

MyCursor = cnx.cursor()

# LISTS AND DEFINITIONS===================================
MenuList = ["CREATE USER", "LOG IN"]
ConfirmList = ["Username","Email","Password"]
# =========================================

# FUNCTIONS ===============================
def Menu():
    global MenuInput
    MenuInput = input("|       WOULD YOU LIKE TO:       |\n|    CREATE USER    |   LOG IN   |\n\n>> ENTER HERE: ").upper()

def Confirm(item,Create_Username,Create_Email,Create_Password2):
    if item == "UserAndEmail":
        print("\n===================================")
        print("|       ACCOUNT INFORMATION       |")
        print("===================================")

        for x in ConfirmList:
            if x == ConfirmList[0]:
                print(f"{x}: {Create_Username}")
            if x == ConfirmList[1]:
                print(f"{x}: {Create_Email}")

        ConfirmNewUserEmail_Bool = input("\n>> Are these Credentials Correct? ").title()
        
        if ConfirmNewUserEmail_Bool == "Yes":
            cnx.commit()

        else:
            print ("\n>>Error")
    
    if item == "Password":
        ConfirmNewUserPassword_Bool = input(f"\nPassword: {Create_Password2}\n>> Is This correct? ").title()
        if ConfirmNewUserPassword_Bool == "Yes":
            cnx.commit()
            cnx.close()
            print("\n==================================")
            print("|         ACCOUNT CREATED        |")
            print("==================================")


            print("\nThank you for registering your account!.\nThis Is the end of regirstration.")
            exit
        else: pass
            # ASK THE USER IF THEY WANT TO MODIFY
            # MODIFY ITEM
    

def CreateUser():
    Create_Username = input(">> Enter USERNAME: ")
    Create_Email = input(">> Enter Email: ")
    Create_Password1 = input(">> Enter Password: ")
    Create_Password2 = input(">> Confirm Password: ")

    if Create_Password1 == Create_Password2:
        Create_Password = Create_Password1
        print(f"\n{Create_Password}")
    
    while Create_Password1 != Create_Password2:
        print("\n>> Your Passwords do not match! Try again. \n")
        Create_Password1 = input(">> Enter Password: ")
        Create_Password2 = input(">> Confirm Password: ")

        if Create_Password1 == Create_Password2:
            Create_Password = Create_Password2

    # ( INSERT USERNAME AND PASSWORD INTO USER_PASSWORD)
    add_User_Email_Q = "INSERT INTO user_email (Username, Email) VALUES (%s, %s)"
    add_User_Email_K = (Create_Username, Create_Email)
        # DO QUARY TO CHECK IF EMAIL MATCHES PREVIOUSLY ENTERED EMAILS
    MyCursor.execute(add_User_Email_Q, add_User_Email_K)
    Confirm("UserAndEmail",Create_Username,Create_Email,Create_Password)
    
    if Create_Password == Create_Password1:
        add_User_Password_Q = "INSERT INTO user_password (Username, Password) VALUES (%s, %s)"
        add_User_Password_K = (Create_Username, Create_Password)
        MyCursor.execute(add_User_Password_Q, add_User_Password_K)
        Confirm("Password",Create_Username,Create_Email,Create_Password)

    
        # ( INSERT USERNAME AND EMAIL INTO USER_EMAIL )


def Signin():
    Login_Username = input("\n>> Enter your Username: ")
    Login_Password = input("\n>> Enter your Password: ")

    Query_Username_Q = "SELECT Username FROM user_email"
    Query_Username_K = (Login_Username)
    MyCursor.execute(Query_Username_Q, Query_Username_K)
    
    MyResult = MyCursor.fetchall()

    for x in MyResult:
        print (x)

    if (Login_Username,Login_Password) in MyCursor:
        print(">> SUCCESSFULLY LOGGED IN <<")
        TimeStamp_Time = time.time()
        TimeStamp_Q = "INSERT INTO logins (Username, Time Stamp) VALUES (%s,%s)"
        TimeStamp_K = (Login_Username,TimeStamp_Time)
        MyCursor.execute(TimeStamp_Q,TimeStamp_K)
        MyCursor.commit()
        MyCursor.close()
    
    if (Login_Username,Login_Password) not in MyCursor:
        Signin_tryagain = ("\nSorry, either the username or password that was entered is either\nincorrect or does not exist. Try again?").title()

        if Signin_tryagain == "Yes":
            Menu()

        if Signin_tryagain == "No":
            cnx.close()

        else:
            Signin_tryagain = input("\nThis is not a valid response. Try again? ")


# =========================================

def main():
    if cnx:
        try: 
            Menu()
            if MenuInput == MenuList[0]:
                CreateUser()
            
            if MenuInput == MenuList[1]:
                Signin()

            while MenuInput not in MenuList:
                print("\n>> This is not an accpetible answer! Try again.\n")
                Menu()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("\nSomething is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("\nDatabase does not exist")
            else:
                print(err)
        else:
            print("\n==================================")
            print("|       CONNECTION CLOSED        |")
            print("==================================\n")
            cnx.close()

if __name__ == '__main__':
    main()

