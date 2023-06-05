n = 1
for i in range(10, 0, -1):
    n *= i
print(n)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


for n in range(0, 21):
    ans = factorial(n)
    print(ans, end=",")
