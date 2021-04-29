def Sorted(array):
    copy = array[::]
    result = []
    while copy:
        minimumElem = min(copy)
        result.append(minimumElem)
        copy.remove(minimumElem)
    return result


print(Sorted([i for i in range(10, 0, -1)]))