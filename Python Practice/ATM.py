balance = 1000.0 #user balance

while True:
    print("""
===============ATM==============

1) CHECK-BALANCE
2) WITHDRAW
3) DEPOSIT
99) EXIT

""")

    try:
        askUser = int(input("ENTER: ").strip())
    except ValueError:
        print("YOU DIDN'T ENTER A VALID NUMBER\n")
        continue

    if askUser == 1:
        print("============================================")
        print(f"\nYOUR CURRENT BALANCE: {balance}")

    elif askUser == 2:
        print("============================================")
        amount = float(input("ENTER AMOUNT TO WITHDRAW: "))
        if amount > balance:
            print("INSUFFICIENT FUNDS")
        else:
            balance -= amount
            print(f"\nYOUR CURRENT BALANCE: {balance}")

    elif askUser == 3:
        print("============================================")
        amount = float(input("ENTER AMOUNT TO DEPOSIT: "))
        balance += amount
        print(f"\nYOUR CURRENT BALANCE: {balance}")

    elif askUser == 99:
        print("THANK YOU, GOODBYE!")
        break

    else:
        print("INVALID CHOICE")   
