n = int(input("enter the value"))
'''for i in range(2,n):
	if n%i==0:
		print("composite")
		break
else:
	print("prime")
for i in range(1,n+1):
	if n%i == 0:
				print(i,"is a factor of",n)
	else:
		print(i,"is not a factor of",n)'''

for i in range(2,n):
		if n%i==0:
			for j in range(2,i):
				if i%j == 0:
					print(i,"is composite factor of",n)
					break
			else:
				print(i,"is prime factor of",n)		


			