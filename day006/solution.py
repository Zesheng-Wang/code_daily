if __name__ == '__main__':
    n = int(input())
    # First method
    for i in range(1, n + 1):
        print(i, end='')

    # line break
    print()

    # Second method
    a = 1
    while a <= n:
        print(a, end='')
        a += 1