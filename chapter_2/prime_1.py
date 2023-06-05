# for n in range(2, 101):
#     for n2 in range(2, n // 2 + 1):
#         if n % n2 == 0:
#             break
#     else:
#         print(n)

for i in range(2, 101):
    h = i // 2
    f = True
    for j in range(2, h + 1):
        if i % j == 0:
            f = False
            break
    if f == True:
        print(i, end=",")
