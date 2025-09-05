'''Create a Python program using functions that calculates the number of days left until the user's next birthday.

The user will input their birth date in the format dd-mm-yyyy.

The program will also ask for today's date in the same format.

You must calculate:

If the birthday has already occurred this year, calculate how many days are left until their next birthday next year.

If the birthday is still coming this year, calculate how many days are left this year.

Show the output in the format:'''

def birthday():
	dob = input("enter your birth date(dd-mm-yy: ")
	day,month,year = dob.split("-")
	return day,month,year
def current_date():
	current_date = input("enter today's date: ")
	day_c,month_c,year_c = current_date.split("-")
	return day_c,month_c,year_c
day,month,year = birthday()
day = int(day)
month = int(month)
year = int(year)


day_c,month_c,year_c = current_date()
day_c = int(day_c)
month_c = int(month_c)
year_c = int(year_c)

birthday_comming_m = month_c - month
if birthday_comming_m<0:
	birthday_comming_m = 12+birthday_comming_m
birthday_comming_d = day_c - day
if birthday_comming_d<0:
	birthday_comming_m = birthday_comming_m-1
	birthday_comming_d = 30 + birthday_comming_d
print("your birthday comming in",birthday_comming_m,"months and" , birthday_comming_d,"days")	 
