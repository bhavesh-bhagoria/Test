def dob():
	dob = input("enter your birth date(dd-mm-yy: ")
	day,month,year = dob.split("-")
	return day,month,year
def current_date():
	current_date = input("enter today's date: ")
	day_c,month_c,year_c = current_date.split("-")
	return day_c,month_c,year_c
day,month,year = dob()
day = int(day)
month = int(month)
year = int(year)


day_c,month_c,year_c = current_date()
day_c = int(day_c)
month_c = int(month_c)
year_c = int(year_c)

age = year_c - year
months = month_c - month
if months<0:
	age = age-1
	months = 12+months
days = day_c-day
if days < 0:
	months = months-1
	days = 30+days
print(age,"years",months,"months and",days,"days")		 

