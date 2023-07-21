amount_of_bills = [10, 10, 10, 10, 10, 10]
after_withdrawal = [10, 10, 10, 10, 10, 10]
action = input("Please enter action ")
while(action!=("Q")) :
    if(action.__eq__("R")) :
        amount_of_bills = [10, 10, 10, 10, 10, 10]
        action = input("What else would you like to do? ")
    elif(action.__eq__("I")) :
        print(amount_of_bills)
        action = input("What else would you like to do? ")
    elif(action[0].upper().__eq__("W")) :
        after_withdrawal = amount_of_bills.copy()
        amt_to_withdraw = int(action[4:len(action)])
        print(amt_to_withdraw)
        while(amt_to_withdraw > 0) :
            if(amount_of_bills[0]  > 0 and amt_to_withdraw >= 100) :
                print(amt_to_withdraw)
                amt_to_withdraw -= 100
                amount_of_bills[0] -= 1
                print(amt_to_withdraw)
                print(after_withdrawal)
            elif(amount_of_bills[1] > 0 and amt_to_withdraw >= 50) :
                amt_to_withdraw -= 50
                amount_of_bills[1] -= 1
                print(after_withdrawal)
            elif(amount_of_bills[2] > 0 and amt_to_withdraw >=20) :
                amt_to_withdraw -= 20
                amount_of_bills[2] -=1
            elif(amount_of_bills[3] > 0 and amt_to_withdraw >=10) :
                amt_to_withdraw -= 10
                amount_of_bills[3] -=1
            elif(amount_of_bills[4] > 0 and amt_to_withdraw >=5) :
                amt_to_withdraw -= 5
                amount_of_bills[4] -=1
            elif(amount_of_bills[5] > 0 and amt_to_withdraw >=1) :
                amt_to_withdraw -= 1
                amount_of_bills[5] -=1
            else:
                print("Insufficient Funds!")
                print(after_withdrawal)
                amount_of_bills = after_withdrawal
                break
        action = input("What else would you like to do? ")
    else:
        action = input("Wrong Command! Please ente a valid command: ")
print("Thanks for coming!")

