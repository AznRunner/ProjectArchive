
month = 0
debt_amount = float(input('Enter total debt amount: '))
rate = float(input('Enter rate amount: '))  

while month >= 0:
    if debt_amount > 0:
     payment = float(debt_amount * rate)
     new_payment = int(debt_amount - payment)
     debt_amount = new_payment
     month += 1
     print(debt_amount)
    elif debt_amount == 0:
      break

print('It will take ' + str(month)+ ' months to pay off the debt')
    




