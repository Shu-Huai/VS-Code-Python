def Sum(elems):
    elemsSum = 0
    for elem in elems:
        elemsSum += elem
    return elemsSum


print(Sum([i for i in range(1, 11)]))