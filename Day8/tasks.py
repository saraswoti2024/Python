#atm machine

balance = 25000
pin2=1234
print("Atm machine".center(50,"*"))
pin1 = int(input("Enter your pin: "))

if pin1==pin2:
        while(True):
            print("-".center(55,"-"))
            choice = int(input("Enter your choice.\n1.balance\n2.deposite\n3.withdraw\n4.Exit:\n "))
            if choice==1:
                print(f"your balance is: {balance}")

            elif choice==2:
                money = float(input("How much money you want to deposite: "))
                balance += money
                print(f"After depositing your total balance is:{balance}")

            elif choice==3:
                withdrawamount = float(input("Enter the amount you want to withdraw: "))
                if(balance<withdrawamount):
                     print("insufficent amount")
                else:
                     balance -= withdrawamount
                     print(f"After withdrawing your total balance is:{balance}")

            elif choice==4:
                break
else:
     print("invalid pin")           