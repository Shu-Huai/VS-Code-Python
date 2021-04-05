#%%
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = numbers[8:6:-1]
print(number)
print(1 in numbers)
length = len(numbers)
maxnumber = max(numbers)
minnumber = min(numbers)
del numbers[9]
print(numbers)
numbers.append(10)
print(numbers)
print(id(numbers))
numbers.append(11)
print(id(numbers))
numbers += [12]
print(id(numbers))
print(id(numbers[0]))
numbers[0] = -1
print(id(numbers[0]))
print(id(numbers))
#%%
import time

start = time.time()
time.sleep(1)
print(time.time() - start)
#%%
x = list("fuck")
print(x)
#%%
x = [[10086] * 2] * 3
print(x)
x[0][0] = 1
print(x)
#%%
x = [1, 2, 1, 2, 1, 1, 1]
for i in x[0:7:1]:
    print(i)
    if i == 1:
        x.remove(i)
        print(x)
try:
    print(x[10])
except IndexError:
    print("No x[10].")
try:
    print(x.index(10))
except ValueError:
    print("No 10 in x.")
print("2 number in x: ", x.count(2))
print("1 number in x: ", x.count(1))
print("3 in x: ", 3 in x)
print("2 not in x: ", 2 not in x)
del x
#%%
List0 = [3, 5, 7, 9, 11]
List1 = ['a', 'b', 'c']
print("3, 'a' in zip: ", (3, 'a') in zip(List0, List1))
for a, b in zip(List0, List1):
    print(a, b)
#%%
s1 = 'programming'
s2 = 'language'
print(s1.capitalize() + ' ' + s2.upper())
#%%
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
freshfruit = [w.strip(" ") for w in freshfruit]
print(freshfruit)
#%%
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vector = [num for elem in vector for num in elem]
print(vector)
#%%
import os

files = [filename for filename in os.listdir(".") if filename.endswith(".py")]
print(files)
del os
#%%
print("Hello World!")
print("Welcome to use Python!")
#%%
import math

print("%.2f" % math.sin(math.radians(30)))
from math import *

print("%.2f" % sin(radians(30)))
from math import sin, radians

print("%.2f" % sin(radians(30)))
#%%
import math

inputString = input("Please input the real and imaginary component of a complex number: ")
a, b = float(inputString.split()[0]), float(inputString.split()[1])
print("The complex number is: ", end="")
if not a and not b:
    print("0.00", end="")
if a:
    print("%.2f" % a, end="")
if b:
    if a:
        if b > 0:
            print(" + ", end="")
        else:
            print(" - ", end="")
    elif b < 0:
        print("-", end="")
    print("%.2fi" % abs(b), end="")
print(".\nThe modulus is: ", end="")
print("%.2f." % math.sqrt(a**2 + b**2))
# %%
fahrenheitDegree = float(input("Please input a degree in Fahrenheit: "))
print("The degree is: %.2f°C" % ((fahrenheitDegree - 32) * 5 / 9))
# %%
inputString = input("Please input the length and the width: ")
a, b = float(inputString.split()[0]), float(inputString.split()[1])
area = a * b
print("The area is: ", end="")
if area == int(area):
    print(int(area))
else:
    print("%.2f" % area)
# %%
inputString = input("Please input three scores: ")
average = (float(inputString.split()[0]) + float(inputString.split()[1]) + float(inputString.split()[2])) / 3
print("The average score is: ", end="")
if average == int(average):
    print(int(average))
else:
    print("%.2f" % average)
# %%
age = input("Please input the age: ")
school = input("Please input the school: ")
experience = input("Please input the experience: ")
major = input("Please input the major: ")
if float(age) <= 25 and school == "Key university." and major == "Finance engineering.":
    print("Excepted.")
elif float(experience) >= 3 and major == "Investment banks.":
    print("Excepted.")
else:
    print("Not excepted.")
#%%
score = int(input("Please input a score: "))
print("The score is: ", end="")
if score >= 90:
    print("A.")
elif score >= 80:
    print("B.")
elif score >= 70:
    print("C.")
elif score >= 60:
    print("D.")
else:
    print("E.")
# %%
inputString = input('Please input the time with 24-hour clock, use the form as "Hour:Minute:Second": ')
hour, minute, second = int(inputString.split(':')[0]), int(inputString.split(':')[1]), int(inputString.split(':')[2])
second = second + 30
minute = minute + 5
if second >= 60:
    second -= 60
    minute += 1
    if minute >= 60:
        minute -= 60
        hour += 1
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
# %%
sum = 0
n = 1
print("n\ts")
while sum <= 1000:
    sum += n**2
    print("%d\t%d" % (n, sum))
    n += 1
n -= 1
if sum > 1000:
    n -= 1
print("The max n is: %d" % n)
# %%
print("The numbers that is divisible by 7 but not by 5 between 0 and 100: ")
formatCount = 0
for i in range(0, 101):
    if not i % 7 and i % 5:
        print(i, end="\t")
        formatCount += 1
        if not formatCount % 5:
            print("\n", end="")
#%%
import random

number = random.randint(0, 9)
guessNumber = -1
while guessNumber != number:
    guessNumber = int(input("Please input a number: "))
    if guessNumber > number:
        print("Too big.")
    if guessNumber < number:
        print("Too small.")
print("Congratulations! You win.")


# %%
def Fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


sum = 0
for i in range(1, 21):
    print("Number %d: " % i, end="")
    print(Fibonacci(i - 1))
# %%
