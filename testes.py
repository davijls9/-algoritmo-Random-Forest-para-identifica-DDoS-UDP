def calculo(n):
    if n == 1:
        return -2
    elif n == 2:
        return 3
    else:
        return calculo(n-1)*calculo(n-2)

print(calculo(5))

