x = {2,32,147,1,66,98}
x = list(x)
print("Given order: ",x)


for i in range(len(x)):
	for j in range(i+1,len(x)):
		if x[i]>x[j]:
			x[i],x[j] = x[j],x[i]
print("Ascending order: ",x)


for i in range(len(x)):
	for j in range(i+1,len(x)):
		if x[i]<x[j]:
			x[i],x[j] = x[j],x[i]
print("Descending order: ",x)				