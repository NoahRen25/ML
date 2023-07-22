action = input("Enter your action: ")

no_withdraw_bills_stocked = [10, 10, 10, 10, 10, 10]
bills_stocked = [10, 10, 10, 10, 10, 10]
bill_values = [100, 50, 20, 10, 5, 1]
def withdraw(amt, value_of_bills, stock_of_bills):
    counter = 0
    overarch_counter = 0
    no_withdraw_bills_stocked = stock_of_bills.copy()
    original_amt = amt
    if(amt==0):
        return original_amt
    elif(amt>0):
        if(overarch_counter <= no_withdraw_bills_stocked[counter]):
            amt -= value_of_bills[counter]
            stock_of_bills -= 1
            overarch_counter += 1
        else:
            counter +=1
            overarch_counter =0
        return withdraw(amt, value_of_bills, stock_of_bills)
    else:
        return withdraw(original_amt, value_of_bills, stock_of_bills[counter] - 1)
while(action.upper() !="Q"):
    if(action.upper()=="I"):
        print(bills_stocked)
        action = input("Enter another action: ")
    elif(action.upper()=="R"):
        bills_stocked = [10, 10, 10, 10, 10, 10]
        action = input("Enter another action: ")
    elif(action[0].upper()=="W"):
        withdrawing = withdraw(action[2:len(action)], bill_values, bills_stocked)
        print("Withdrawn: " + str(withdrawing))
        action = input("Enter another action: ")
        
    else:
        print("Invalid action! Please enter another action")




