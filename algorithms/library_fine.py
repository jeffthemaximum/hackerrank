import datetime

line1 = raw_input()
line2= raw_input()

line1 = [int(x) for x in line1.split(" ")]
line2 = [int(x) for x in line2.split(" ")]

turnin = datetime.date(line1[2], line1[1], line1[0])
due = datetime.date(line2[2], line2[1], line2[0])

fine = 0

if (turnin <= due):
    pass
elif (turnin.month == due.month and turnin.year == due.year):
    day_dif = turnin.day - due.day
    fine = 15 * day_dif
elif (turnin.year == due.year):
    month_dif = turnin.month - due.month
    fine = 500 * month_dif
else:
    year_dif = turnin.year - due.year
    fine = 10000 * year_dif

print fine