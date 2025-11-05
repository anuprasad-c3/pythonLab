import time
import datetime
current_datetime = datetime.datetime.now()
current_time = time.localtime()

print("a) Current date and time :",current_datetime)
print("b) Current year :",current_datetime.year)
print("c) Month of the year :",current_datetime.strftime("%B"))
print("d) Week number of the year :",time.strftime("%U",current_time))
print("e) Day of year :",current_datetime.strftime("%j"))
print("f) Day of the month :",current_datetime.day)
print("g) Day of week(0=Monday) :",current_datetime.weekday())
