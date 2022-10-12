# Calculate year of birth
import datetime

day = 0
month = 0
year = 0

while True:
    day = input("Input day you were born (e.g. 12): ")
    if day.isdigit():
        while True:
            month = input("Input month you were born (e.g. 5): ")
            if month.isdigit():
                while True:
                    year = input("Input year you were born (e.g. 1999): ")
                    if year.isdigit():
                        break
                    else:
                        print("Invalid entry")
                        continue  # not needed but to clarify
                break
            else:
                print("Invalid entry")
                continue  # not needed but to clarify
        break
    else:
        print("Invalid entry")
        continue  # not needed but to clarify

date_today = datetime.date
print(date_today.today())

day_today = int(str(date_today.today())[-2:])
month_today = int(str(date_today.today())[5:7])
year_today = int(str(date_today.today())[:4])

month = int(month)
day = int(day)
year = int(year)

# print(day_today)
# print(month_today)
# print(year_today)

years_old = int(year_today) - year
months_old = 0
days_old = 0
if month > month_today:
    months_old = month - month_today
    days_old = day - day_today + 31  # 31 as october is 31 days, 28 if feb and 30 if month is 30 days
    years_old -= 1
elif month == month_today and day > day_today:
    days_old = day - day_today
    years_old -= 1
else:
    print("error")
age = [days_old, months_old, years_old]
print(f"Days old: {days_old}\nMonths old: {months_old}\nYears old: {years_old}")
