if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        if 2 < n < 5:
            print('Hello Python！')
        elif 6 < n <= 20:
            print('Hello World！')
        elif n > 20:
            print('Hello Python！')
    else:
        print('Hello World！')