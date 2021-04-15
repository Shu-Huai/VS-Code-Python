inputString = input('Please input the time with 24-hour clock, use the form as "Hour:Minute:Second": ')
hour, minute, second = int(inputString.split(':')[0]), int(inputString.split(':')[1]), int(inputString.split(':')[2])
second = second + 1
if second == 60:
    second = 0
    minute = minute + 1
    if minute == 60:
        minute = 0
        hour = hour + 1
        if hour == 24:
            hour = 0
if hour < 10:
    hour = str("0") + str(hour)
else:
    hour = str(hour)
if minute < 10:
    minute = str("0") + str(minute)
else:
    minute = str(minute)
if second < 10:
    second = str("0") + str(second)
else:
    second = str(second)
print("The time after one second is: " + hour + ":" + minute + ":" + second)