"""var_a = []
n = int(input("enter the number of values:"))
for i in range(n):
	x = int(input("enter numbers: "))
	var_a.append(x)
	print(var_a)
"""



'''n = int(input("Enter the No. of Values to be taken : "))
item_list = []

for i in range(n) :
	item = int(input("Enter Item Value : "))
	item_list.append(item)

print(item_list)

sum_value = 0
for j in range(len(item_list)):
	sum_value += item_list[j]

average = sum_value/n 

#print("Average of {} = {}".format(item_list,average))
print("Average of ",item_list,"=",average)'''
var_a = ["Bhavesh","20","Indore","bhaveshbhagoria@gmail.com"]
'''for i in var_a:
	print(i)'''
y = var_a.index("Bhavesh")
print(y)
var_a[y] = "Bhavesh123"
print(var_a)
var_a.pop()   #last wala remove
var_a.remove(21)
