import sympy

sympy.init_printing(use_unicode=True)
x = sympy.symbols("x")
expression = (1 + x**2)**3
print("The expression is: ", end="")
print(sympy.integrate(expression, x))