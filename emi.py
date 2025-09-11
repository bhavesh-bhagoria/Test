
p = float(input("enter the principal amnt"))
r = float(input("enter the rate of intrest"))
t = int(input("enter the time tenure in years"))
si = (p*r*t)/100
total_payable = si+p
emi = total_payable/(t*12)
tl = (t*12)
balance = total_payable
print("Simple intrest for the loan wll be: ","₹",round(si,2))
print("Total payable amount will be","₹",round(total_payable,2))
print("EMI per month will be","₹",round(emi,2))
print("_________________________________________")
for i in range(1,tl+1):
	total_payable = si+p
	intrest_per_month = emi-(p/(t*12))
	principle_per_month = p/(t*12)
	balance = balance - emi
	print("Installment:", i ,"-:","₹",round(emi,2))
	print("principal paid: ","₹",round(principle_per_month,2))
	print("Intrest paid: ","₹",round(intrest_per_month,2))
	print("Remaining amount: ","₹",round(balance,2))																						
	print("_________________________________________")