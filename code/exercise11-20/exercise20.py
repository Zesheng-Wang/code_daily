def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(str(i).rjust(w, ' '), end=' ')  # 十进制数
        print(oct(i)[2:].rjust(w, ' '), end=' ')  # 八进制数
        print(hex(i)[2:].rjust(w, ' '), end=' ')  # 十六进制数
        print(bin(i)[2:].rjust(w, ' '), end=' ')  # 二进制数
        print()


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)