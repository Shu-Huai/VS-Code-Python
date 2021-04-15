from random import randint
from matplotlib import pyplot as plt


def GetFrequency(classNum, studentNumPerClass):
    birthdays = []
    for i in range(classNum):
        birthdays.append([])
        for j in range(studentNumPerClass):
            month = randint(1, 12)
            if month == 2:
                day = randint(1, 28)
            elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                day = randint(1, 31)
            else:
                day = randint(1, 30)
            birthdays[i].append({"month": month, "day": day, "class": i})
    sum = 0
    tag = 0
    for i in range(classNum):
        for j in range(studentNumPerClass):
            for birthday in birthdays[i]:
                if birthday == birthdays[i][j] and birthday is not birthdays[i][j]:
                    sum += 1
                    tag = 1
                    break
            if tag:
                tag = 0
                break
    return sum / classNum


classNum = int(input("Please input the class number: "))
studentNumPerClass = int(input("Please input the student number: "))
print("The frequency is: %f" % GetFrequency(classNum, studentNumPerClass))
x = []
y = []
for i in range(20):
    x.append(i * 5)
    y.append(GetFrequency(5000, i * 5))
fig = plt.figure()
fig.suptitle("The frequency and the student number per class", fontsize=14)
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel("Student number per class")
ax.set_ylabel("Frequency")
ax.plot(x, y)
plt.show()