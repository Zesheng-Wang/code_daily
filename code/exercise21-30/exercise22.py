n = int(input())
# count = 0
# s = 0
for x in range(n // 5):
    y = (2 * n - 14 * x) / 8
    z = n - y - x
    if z == int(z) and y >= 0 and z >= 0:
        # count += 1
        # s += x
        print(x, y, z)
# if count > 0:
#     print(count, s)
# else:
#     print(0, -1)