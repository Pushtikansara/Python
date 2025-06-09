
import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

current_hour = int(time.strftime('%H'))

if current_hour < 12:
    print("Good Morning")
elif current_hour >= 12 and current_hour < 17:
    print("Good Afternoon")
else:
    print("Good Evening")
