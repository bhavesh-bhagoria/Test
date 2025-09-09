n = int(input("enter number of digits: "))
def avg(n):
	sum = 0
	for i in range(n):
		x = int(input("enter number"))
		sum = sum+x
		avrage = sum/n 
	return avrage
print(avg(n))
