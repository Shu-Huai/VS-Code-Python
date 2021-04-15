number = int(input("Please input a number: "))
if number > 99 and number < 1000:
    print("Hundreds: ", number // 100, " Tens: ", number // 10 % 10, " Ones: ", number % 10)
import math

numbers = input("Please input a, b, and angle: ")
a, b, angle = float(numbers.split()[0]), float(numbers.split()[1]), float(numbers.split()[2])
if a > 0 and b > 0 and angle > 0:
    print("c is: ", math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle * math.pi / 180)))
words = input("Please input three words: ")
a, b, c = sorted([words.split()[0], words.split()[1], words.split()[2]])
print(a, b, c)
import os
import sys
import datetime

head = '#' + '- ' * 20 + '\n' +\
 '#Function description:\n' +\
  '#' + '-' * 20 + '\n' +\
   '#Author: Dong Fuguo\n' +\
    '#QQ: 306467355\n' +\
     '#Email: dongfuguo2005@ 126. com\n' +\
      '#' + '-' * 20 + '\n'
desFile = sys.argv[1]
if os.path.exists(desFile) or not desFile.endswith('.py'):
    print('%s already exist or is not a Python code file.!' % desFile)
    sys.exit()
fp = open(desFile, 'w')
today = str(datetime.date.today())
fp.write('#- * -coding:utf-8 - * -\n')
fp.write('#Filename: ' + desFile + '\n')
fp.write(head)
fp.write('#Date:' + today + '\n')
fp.write('#' + '-' * 20 + '\n')
fp.close()