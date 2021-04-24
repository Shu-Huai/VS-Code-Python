from math import pi
from math import sqrt
from math import factorial

sum = 0
for k in range(3):
    sum += factorial(4 * k) * (1103 + 26390 * k) / factorial(k)**4 / 396**(4 * k)
calculatedPi = 1 / (sum * 2 * sqrt(2) / 9801)
print("The pi in math is: %.15f.\nThe pi in formula is: %.15f." % (pi, calculatedPi))
