import copy


def Ackermann(m, n):
    if not m:
        return n + 1
    if m > 0 and not n:
        return Ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return Ackermann(m - 1, Ackermann(m, n - 1))


def DeleteRepeat(elems):
    result = copy.deepcopy(elems)
    result.clear()
    noRepeat = set()
    for elem in elems:
        originalLength = len(noRepeat)
        noRepeat.add(elem)
        if len(noRepeat) != originalLength:
            result.append(elem)
    return result


print("Ackermann(3, 4) = %d." % Ackermann(3, 4))
testList = [0, 0, 1, 2, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9, 9, 9]
print("The original list is: %s" % testList)
print("After deleted repeat, it is: %s" % DeleteRepeat(testList))