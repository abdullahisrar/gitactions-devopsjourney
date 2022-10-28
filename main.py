def factor(n):
    result = 1
    for i in range(result, n + 1):
        result = result * i
    return result


print(factor(4))
print(factor(5))
