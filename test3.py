balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
start = balance
total = 0
month = 1
while month < 13 :
	
	
	
	
	Remaining_balance = 0
	Previous_balance = balance - Remaining_balance
	MonthlyInterestRate= (annualInterestRate) / 12.0
	Minimum_monthly_payment = (monthlyPaymentRate) * (Previous_balance)
        total= total + Minimum_monthly_payment
	Monthly_unpaid_balance = (Previous_balance) - (Minimum_monthly_payment)
	Remaining_balance = (Monthly_unpaid_balance) + (MonthlyInterestRate * Monthly_unpaid_balance)
	
        balance = Remaining_balance
	print("Month:", month)
	print("Minimum_monthly_payment:" , round(Minimum_monthly_payment,2))
	
	print("Remaining balance:" ,round(Remaining_balance,2))
        
	month = month + 1
	


print("Total paid:" ,round(total,2))
print("Remaining balance:" ,round(Remaining_balance,2))
