def solve(s):
    return ' '.join(i.capitalize() for i in s.split(' '))


if __name__ == '__main__':
    s = input()

    result = solve(s)
    print(result)
