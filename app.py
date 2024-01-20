
def login_and_registration():
    s = input("\nAre you an existing user (y/n): ")
    if s.lower() == 'y':
        while True:
            user_name = input("Enter your username: ")
            password = input("Enter your password: ")
            validation(user_name, password)
            if validation(user_name, password):
                print("you have successfully logged in")
                break
            else:
                print("login failed, please try again")

    else:
        while
        user_name = input("please enter your username: ")
        while True:
            password = input()
            confirm_password = input()

            if password != confirm_password:
                print("Both Passwords dont match, please try again")
            else:
                break


def validation(user_name, password):

def open_account():

def close_account():

def deposit_money():

def withdraw_money():

def main():
    print("Welcome to the Bank Management App\n")
    login_and_registration()

    # add a login and registration module
    print("Your options are: \n")
    print("0 - Quit")
    print("1 - Open an account")
    print("2 - Close an account")
    print("3 - Deposit Money")
    print("4 - Withdraw Money\n")
    s = input("Please enter your option: ")

    while(True):
        if s == '0':
            break;
        elif s == '1':
            open_account()
        elif s == '2':
            close_account()
        elif s == '3':
            close_account()
        elif s == '4':
            close_account()


main()

