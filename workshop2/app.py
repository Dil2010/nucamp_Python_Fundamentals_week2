from banking_pkg.account import*

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

while True:
    print("          === Automated Teller Machine ===          ")
    name=input("Enter name to register:" )
    if len(name)>10:
        print("The maximum length is 10 characters")
        name=input("Enter name to register:" )
    if len(name)==0:
        print("You must enter a name")
        name=input("Enter name to register:" )
    pin=input("Enter PIN: ")
    if len(pin)!=4:
        print("Pin must contain four numbers")
        pin=input("Enter PIN: ")
    balance=0
    print(name, "has been registered with a starting balance of $",balance)
    break

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate=input("Enter name:")
    pin_to_validate=input("Enter pin:")
    if name_to_validate==name and pin_to_validate==pin:
        print("Login Successful!")
        break
    else:
        print("Invalid Credential")
    
while True:
    atm_menu(name)
    option=input("Choose an Option:")
    if option=="1":
        show_balance(balance)
    elif option=="2":
        balance=deposit(balance)
    elif option=="3":
        balance=withdraw(balance)
    elif option=="4":
        logout(name)
        break
    else:
        print("Wrong Choice!,Choose an option between 1-4")



