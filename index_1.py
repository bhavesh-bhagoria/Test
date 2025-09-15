from phonebook_functions_1 import *


def main_opt() :
	print("=============================") 	
	opt_choice = input("Press 1 for Creating a Contact\nPress 2 for Searching a Contact\nPress 3 for Display all contact\nPress 4 for Updating a Contact\nPress 5 for Deleting a Contact\nEnter a Valid Choice : ")
	print("=============================")
	if opt_choice == "1":
		create_contact()
	elif opt_choice == "2":
		search_contact()
	elif opt_choice == "3":
		display_all_contact()
	elif opt_choice == "4":
		update_contact()
	elif opt_choice == "5":
		delete_contact()
	else : 
		print("Invalid Choice. Please restart the program")
		main_opt()
	print("=============================")


print("Welcome to My Phonebook")
main_opt()