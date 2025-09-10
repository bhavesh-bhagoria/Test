n = int(input("enter number : "))
temp = n
result = 0
while n >0:
	last_digit = n%10
	print(last_digit)
	n = n//10
	result = result + last_digit**len(str(temp))
if result == temp:
	print("The number is astronomical")	
	

