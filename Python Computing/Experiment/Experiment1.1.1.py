Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.version
'3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]'
>>> sys.winver
'3.9'
>>> sys.version_info
sys.version_info(major=3, minor=9, micro=2, releaselevel='final', serial=0)
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sys']
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 15151515151515151515*33333333333333333333
505050505050505050494949494949494949495
>>> 2016**2016

>>> 23+3
26
>>> 23>3
True
>>> '23'+'3'
'233'
>>> 23/3
7.666666666666667
>>> 23//3
7
>>> 23%3
2
>>> 23**3
12167
>>> 23+24.5
47.5
>>> 23+'3'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    23+'3'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
2
>>> 23+int('3')
26
>>> 'hello'+str("123")
'hello123'
>>> int(23/3)
7
>>> round(23/3,2)
7.67
>>> round(23/3)
8
>>> 0<23<100
True
>>> s1='programming'
>>> s2='language'
>>> s1[1]
'r'
>>> s1[:4]
'prog'
>>> s1[0]+s2[1:3]
'pan'
>>> s1.capitalize()+' '+s2.upper()
'Programming LANGUAGE'
>>> s1.count('r')
2
>>> s1.count('p')
1
>>> s1
'programming'
>>> s1.count('r')+s1.find('r')+s1.rfind('r')
7
>>> s3=s2.join('--')
>>> s4='-'.join(s2)
>>> L1=s4.split()
>>> 3*(s2[:2]+' ')
'la la la '
>>> "Python"+s2.rjust(10)
'Python  language'
>>> help()

Welcome to Python 3.9's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> help(int)

>>> help('str')

>>> help(str)

>>> help(sys)

>>> help(s1)
No Python documentation found for 'programming'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help(round)
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.

>>> ord("A")
65
>>> str(65)
'65'
>>> str("A")
'A'
>>> str(A)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    str(A)
NameError: name 'A' is not defined
>>> import math
>>> dir()
['L1', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'math', 's1', 's2', 's3', 's4', 'sys']
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
>>> import random
>>> a=[random.randint(1,100) for i in range(10)]
>>> max(a)
79
>>> min(a)
8
>>> sum(a)/10
42.7
>>> 