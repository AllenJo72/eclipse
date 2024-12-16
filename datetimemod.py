import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

current_date = datetime.date.today()
print("Current date:", current_date)

current_time = now.time()
print("Current time:", current_time)


year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print(f"Year: {year}, Month: {month}, Day: {day}, Hour: {hour}, Minute: {minute}, Second: {second}")
