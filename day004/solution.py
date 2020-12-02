if __name__ == '__main__':
    n = int(input())
    # first : use range
    for i in range(0, n):
        print(i ** 2, end=' ')

    print('\n')

    # second : flag
    i = 0
    while i < n:
        print(i ** 2, end=' ')
        i += 1