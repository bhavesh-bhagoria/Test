import menu_list_function as mlf
#this is the sample change 
def select():
	choice = int(input("Press 1 for add\nPress 2 for sub\nPress 3 for mul\nEnter a valid choice : "))
	if choice == 1 :
		result = mlf.addition()
		print(result)
	elif choice == 2 :
		result = mlf.substraction()
		print(result)
	elif choice == 3 :
		result = mlf.multiplication()
		print(result) 	
	else : 
		print("Invalid Choice")
		select()

select()