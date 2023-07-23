action = input("Enter your action: ")

no_withdraw_bills_stocked = [10, 10, 10, 10, 10, 10]
bills_stocked = [10, 10, 10, 10, 10, 10]
bill_values = [100, 50, 20, 10, 5, 1]
def withdraw(amt, original_amt, over_counter, counter, iterations, iter_count, value_of_bills, stock_of_bills, orig_stock):
    if(amt == 0):
       if(iterations>0):
        temp = orig_stock[iter_count] - iterations
        stock_of_bills[iter_count] = orig_stock[iter_count] - temp
       return original_amt, stock_of_bills
    elif(amt > 0 and counter <= 5):
       if(amt >= value_of_bills[counter] and stock_of_bills[counter] >0):
           amt -= value_of_bills[counter]
           stock_of_bills[counter] -= 1
           return withdraw(amt, original_amt, over_counter, counter, iterations, iter_count, value_of_bills, stock_of_bills, orig_stock)
       else:
           return withdraw(amt, original_amt, over_counter, counter + 1, iterations, iter_count, value_of_bills, stock_of_bills, orig_stock)
    elif(iterations < orig_stock[iter_count]):
        iterations += 1
        stock_of_bills = orig_stock.copy()
        stock_of_bills[iter_count] -= iterations
        if(iterations == orig_stock[iter_count]):   
            return withdraw(original_amt, original_amt, over_counter, over_counter, 0, iter_count + 1, value_of_bills, stock_of_bills, orig_stock)
        return withdraw(original_amt, original_amt, over_counter, over_counter, iterations, iter_count, value_of_bills, stock_of_bills, orig_stock)
    elif(over_counter < 5):
       over_counter +=1
       return withdraw(original_amt, original_amt, over_counter, 0 + over_counter, 0, 0, value_of_bills, orig_stock.copy(), orig_stock)
    else:
        return 'Failed: Insufficient Balance', orig_stock
while(action.upper() !="Q"):
    if(action.upper()=="I"):
        print(bills_stocked)
        action = input("Enter another action: ")
    elif(action.upper()=="R"):
        bills_stocked = [10, 10, 10, 10, 10, 10]
        action = input("Enter another action: ")
    elif(action[0].upper()=="W"):
        withdrawing = withdraw(int(action[2:len(action)]), int(action[2:len(action)]), 0, 0, 0, 0, bill_values, bills_stocked, bills_stocked.copy())
        print("Withdrawn: ", str(withdrawing[0]))
        bills_stocked = withdrawing[1]
        action = input("Enter another action: ")
        
    else:
        action = input("Invalid action! Please enter another action")




