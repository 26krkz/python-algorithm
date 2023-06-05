a = [10, -5, 0, 29, 6, 2, 77, 8]
for n in a:
    if n % 2 == 0:
        print(f"{n} is a even")
    else:
        print(f"{n} is a odd")

for n in range(1, 5 + 1):
    two = 2
    three = 3
    for j in range(1, n + 1):
        two *= 2
        three *= 3
    print(three - two)

for n in range(1, 6):
    v1 = 3**n
    v2 = 2**n
    print("3の{}乗と2の{}乗の差は{}".format(n, n, v1 - v2))
