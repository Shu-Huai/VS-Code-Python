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
scoreSum = 0
n = 1
print("n\ts")
while scoreSum <= 1000:
    scoreSum += n**2
    print("%d\t%d" % (n, scoreSum))
    n += 1
n -= 1
if scoreSum > 1000:
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


scoreSum = 0
for i in range(1, 21):
    print("Number %d: " % i, end="")
    print(Fibonacci(i - 1))
# %%
i = 100
while i >= 100 and i < 1000:
    if (i // 100)**3 + (i % 100 // 10)**3 + (i % 10)**3 == i:
        print(i)
    i += 1
# %%
n = int(input("Please input a number: "))
n -= n % 23
if n <= 0:
    n = 0
print("The max number is: %d" % n)
# %%
formatCount = 0
for i in range(2, 1000):
    flag = 0
    for j in range(2, i):
        if not i % j:
            flag = 1
            break
    if not flag:
        print("%3d" % i, end=" ")
        formatCount += 1
        if not formatCount % 10:
            print("\n", end="")
# %%
c = 0
while c != "#":
    c = input("Please input a char: ")
    if c != "#":
        print("The char is: %s" % c)
print("Input ends.")
# %%
inputList = []
oddSum = 0
evenSum = 0
while not len(inputList) or inputList[len(inputList) - 1] != -1:
    n = int(input("Please input a number: "))
    inputList.append(n)
    if n == -1:
        pass
    elif n % 2:
        oddSum += n
    else:
        evenSum += n
inputList.pop()
print("The list is: ", end="")
print(inputList)
print("The odd sum = %d, the even sum = %d." % (oddSum, evenSum))
# %%
scoreList = [68, 75, 32, 99, 78, 45, 88, 72, 83, 78]
scoreLevel = dict(Excellent=0, Good=0, Middle=0, Bad=0)
for score in scoreList:
    if score >= 90 and score <= 100:
        scoreLevel["Excellent"] += 1
    elif score >= 80 and score <= 89:
        scoreLevel["Good"] += 1
    elif score >= 60 and score <= 79:
        scoreLevel["Middle"] += 1
    elif score >= 0 and score <= 59:
        scoreLevel["Bad"] += 1
for i in range(len(scoreLevel)):
    print(list(scoreLevel.keys())[i], end="")
    print(": ", end="")
    print(list(scoreLevel.values())[i], end="")
    if i == len(scoreLevel) - 1:
        print(".\n", end="")
    else:
        print(", ", end="")
# %%
scoreSum = 0
max = -1
min = 121
count = 0
n = 0
while n != -1:
    n = float(input("Please input a score, ends with -1: "))
    if n == -1:
        break
    if n > max:
        max = n
    if n < min:
        min = n
    scoreSum += n
    count += 1
print("The average score is: %.2f.\nThe max score is: %.2f.\nThe min score is: %.2f." % (scoreSum / count, max, min))
# %%
count = 0
numbers = []
while count < 10:
    a = int(input("Please input ten numbers: "))
    if a % 2 != 0:
        numbers.append(a)
        count += 1
    else:
        print("输入的不是奇数")
print("The list is: ", numbers)
print("The sum is: ", sum(numbers))
print("The average is: ", sum(numbers) / len(numbers))
# %%
stringList = ["Beautiful is better than ugly.", "Explicit is better than implicit.", "Simple is better than complex.", "Complex is better than complicated."]
inputString = input("Please input the start and end: ")
startIndex, endIndex = int(inputString.split()[0]), int(inputString.split()[1])
for string in stringList:
    print("The string is: %s, the length is: %d, the substring is: %s." % (string, len(string), string[startIndex - 1:endIndex]))
# %%
string = input("Please input a string: ")
print("The new string is: %s" % string[::2])
# %%
inputString = input('Please input the temperatures, splitting with ", ": ')
temperatureList = inputString.split(", ")
temperatureSum = 0
for temperature in temperatureList:
    temperatureSum += float(temperature)
print("The average temperature is: %.2f." % (temperatureSum / len(temperatureList)))
# %%
string = input("Please input a string: ")
capitalChar = 0
smallChar = 0
number = 0
other = 0
for char in string:
    if char > 'A' and char < 'Z':
        capitalChar += 1
    elif char > 'a' and char < 'z':
        smallChar += 1
    elif char > '0' and char < '9':
        number += 1
    else:
        other += 1
print("The capital char is: %d, the small char is: %d, the number is: %d, the other is: %d." % (capitalChar, smallChar, number, other))


# %%
def PrintChars(startChar, endChar, number):
    outputChar = startChar
    formatCount = 0
    while outputChar <= endChar:
        print(outputChar, end=" ")
        outputChar = chr(ord(outputChar) + 1)
        formatCount += 1
        if not formatCount % number:
            print("\n", end="")


print("The output is:")
PrintChars("!", "9", 10)


# %%
def IsPrime(number):
    if number < 2:
        raise Exception
    for i in range(2, number):
        if not number % i:
            return 0
    return 1


number = int(input("Please input a number: "))
try:
    if IsPrime(number):
        print("%d is prime." % number)
    else:
        print("%d is not prime." % number)
except Exception:
    print("%d is not prime and not prime." % number)


# %%
def TestDefalt(a=0):
    print(a)


b = 0
TestDefalt(b=10)


# %%
class A(object):
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('__private() method in A')

    def public(self):
        print('public() method in A')


class B(A):
    def __init__(self):
        A.__init__(self)
        self.__private()
        self.public()

    def __private(self):
        print('__private() method in B')

    def publicB(self):
        print('public() method in B')


a = A()
b = B()
print(dir(a))
print(dir(b))

# %%
