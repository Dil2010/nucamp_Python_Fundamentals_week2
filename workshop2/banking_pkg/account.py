def show_balance(balance):
    print(f"Current Balance: ${balance}")

def deposit(balance):
    amount=input("Enter amount to deposit:")
    balance_float=float(balance)
    amount_float=float(amount)
    balance_float=balance_float+amount_float
    print(f"Current Balance: ${balance_float}")
    return balance_float

def withdraw(balance):
    amount=input("Enter amount to withdraw:")
    balance_float=float(balance)
    amount_float=float(amount)       
    if balance_float < amount_float:
        print("Insufficient balance")
    else:
        balance_float=balance_float-amount_float 
        print(f"Current Balance: ${balance_float}")
    return balance_float

def logout(name):
    print("Goodbye",name)

