secret = 7 
guess = " "
limit = 0
i = 5

while i>limit:
    print("-".center(50,"-"))
    guess = int(input("Enter your Guess: "))

    if (guess==secret):
        print("you won!")
        choice = input("Do you want to play again Y or N: ").upper()
        if choice=='Y':
            i = 5
            continue
        elif choice=='N':
            break
        else:
            print("write Y or N")

    else:
        i -= 1
        print(f"you have {i} choices left")
        if i ==0:
            print("you lose!")
            print("-".center(50,"-"))
            choice = input("Do you want to play again Y or N: ").upper()
            if choice=='Y':
                i = 5
                continue
            elif choice=='N':
                break
            else:
                print("write Y or N")
            
print("-".center(50,"-"))
print("Game Over!")
