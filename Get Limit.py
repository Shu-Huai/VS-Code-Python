import sympy

x, y = sympy.symbols("x y")
expression = sympy.exp((-1 / (y**2 - x**2)))
print("The limit is ", end="")
print(sympy.limit(sympy.limit(expression, x, 1 / sympy.sqrt(y)), y, sympy.oo))