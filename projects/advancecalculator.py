def operation1(num1,operation,num2):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        return num1/num2

symbols = {
    "+" : "addition",
    "-": "subtraction",
    "*" : "multiplication",
    "/" : "division"
}

def overall():
    print("Advance Calculator".center(50,"-"))
    num1 = float(input("Enter num1: "))

    while(True):                        #5+2 #result-7 , 5+2=7 , question-y , num1 = 7 ,  op = - , num2 = 2 , res = 5
        # print(symbols.keys())
        for keys in symbols:
            print(keys)
        operation = (input("pick an operation: "))

        if operation not in symbols: 
            print("only pick a symbol provided")
            overall()

        num2 = float(input("Enter num2: "))
        result = operation1(num1=num1,operation=operation,num2=num2)
        print(f"{num1} {operation}{num2} = {result}")

        question = input(f"Enter 'y' Do you want to continue calculation with {result} or 'n' to start new calculation or 'x' to exit: ").lower()

        if question == 'y':
            num1 = result

        elif question=='n':
            overall()

        elif question=='x':
            break

        else:
            print("write y or n or x")
            break
overall()