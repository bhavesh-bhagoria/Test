'''n = int(input("enter number : "))
count = 0 #space complexity is S(1) because there are only two var and it dosn't depend on length of input
while n >0:
	last_digit = n%10
	print(last_digit)
	n = n//10     #for time complexity o(log to the base wo hoga jo divide ho raha iteratable variable me here it is 10(N)where N is number of terms in input) {O(log10(N))}
	count+=1
print("count: ",count)

'''