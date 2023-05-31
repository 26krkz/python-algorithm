def addup(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


res = addup(10)
print(res)


def addup2(n):
    return (1 + n) * (n / 2)


res = addup2(10)
print(res)


for i in range(1, 10):
    k = ""
    for j in range(1, 10):
        k += "{}*{}={:2d} ".format(j, i, i * j)
    print(k)
