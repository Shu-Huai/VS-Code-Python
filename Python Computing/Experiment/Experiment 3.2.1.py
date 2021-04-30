def Ackermann(m, n):
    if not m:
        return n + 1
    if m > 0 and not n:
        return Ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return Ackermann(m - 1, Ackermann(m, n - 1))


print("Ackermann(3, 4) = %d." % Ackermann(3, 4))