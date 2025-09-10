def avg(a,b):
	sum=0
	for i in range(n):
		sum=a+b
		avg=sum/2 
		print("avg",avg)
		return sum
n=int(input("enter number 1: "))
y=int(input("enter nummber 2: "))
x = avg(n,y)
print(x)