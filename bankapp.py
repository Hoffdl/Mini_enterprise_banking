import math
print("Welcome to Daemon banking application, please signup to continue using our services.")
def signup():
    global name # Username
    global pin # Password
    global currentbalance # Current Balance
    name = str(input("Create a username: "))
    pin = str(input("Create a 6 digit pin: "))
    if len(pin) == 6:
        pin = pin
    else:
        print("The pin has to be in 6 digits, try again!!")
        newpin = str(input("Create a 6 digit pin: "))
        if len(newpin) != 6:
            print("The pin has to be in 6 digits, try again!!")
            signup()
        else:
            pin = newpin
    print("Your account has been created successfully..")

def forgotpin():
    recoverypin = str(input("Create a new 6 digit pin: "))
    if len(recoverypin) != 6:
        print("The pin has to be in 6 digits, try again!!")
        forgotpin()
    else:
        print("Your pin has been updated, please login..")
        pin = recoverypin
        login()

def login():
    # name1 represents username
    # pin1 represents user's pin
    name1 = str(input("Enter your username: "))
    pin1 = str(input("Enter your pin: "))
    # Check if the name and pin matches
    if name1 == name and pin1 == pin:
        print("Login Successful.. ")
        print("Welcome to Daemon online banking app" + " " + name)

        print("Please choose a menu below")
        listmenu = ("1-Deposit","2-Withdraw","3-Transfer","4-Check balance")
        for a in listmenu:
            print(a)
        choose = int(input("Enter your choice: "))
        d = 0 # d represents deposit
        w = 0 # w represents withdraw
        cb = 0 # cb rep2resents current balance
        if choose == 1:
            d = int(input("Enter deposit amount: "))
            cb = d
            print(("Your current balance is" +" "+ str(cb)))
        elif choose == 2:
            w = int(input("Enter withdrawal amount: "))
            if w > cb:
                print("Current balance not sufficient for this transaction")
                login()
            else:
                cb = d-w
                print(str(w) +" "+ "has been withdrawn from your account" " and your current balance is" +" "+ str(cb))
        elif choose == 3:
            dest = str(input("Please enter recepient account number: "))
            if len(dest) == 10:
                amount = int(input("Please enter transfer amount: "))
                if amount > cb:
                    print("Insufficient amount to perform this transaction, try again..")
                    login()
                else:
                    cb = d - amount
                    print("The sum of" + " " + str(amount) + " " + "has been transferred to" + " " + str(dest) + " " + "your current balance is" + str(cb))
                    
        elif choose == 4:
            print("Your current balance is" + " " + str(cb))
    else:
        print("Either your username or pin is incorrect, did you create an account? ")
        list1 =["1-Y","2-N"]
        for i in list1:
            print(i)
        inp = int(input("Enter your choice below: "))
        if inp == 1:
            list2 = ["1-Login again","2-Forgot your pin"]
            for e in list2:
                print(e)
            theanswer = str(input("Please enter your choice: "))
            theanswer = int(theanswer)
            if theanswer == 1:
                login()
            elif theanswer == 2:
                forgotpin()
            else:
                print("Option is not available")
                login()
        elif inp == 2:
            print("Please create your account first")
            signup()
    exit()

def mainmenu():
    options = int(input("Choose 1 to signup and choose 2 to login: "))
    if options == 1:
        signup()
    elif options == 2:
        login()
    else:
        print("Option is not available")
        mainmenu()
    exit()

def exit():
    finish = str(input("Do you still want to continue transaction? Y or N: "))
    if finish == "Y":
        login()
    elif finish == "N":
        print("Thank you for using this app")
    else:
        print("Option is not available")
        mainmenu()

mainmenu()