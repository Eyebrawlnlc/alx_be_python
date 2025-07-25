import datetime

date = datetime.datetime.now()
print("Current date and time:", date.strftime("%Y-%m-%d %H:%M"))

time = date.strftime("%H:%M")
print("Current time:", time)