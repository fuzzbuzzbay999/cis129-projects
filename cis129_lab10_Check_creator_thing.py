#PROD USER FOR CASH AMOUNT TO PUT ON THE CHECK
amount=float(input('Enter in the dollar amount you want for the check'))
#Format abd print the amount with 10 numbers (1 for the .) and fill the remaining with *
print(f'{amount:>11.2f}'.replace(' ','*'))
