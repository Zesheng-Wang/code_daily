def wrap(string, max_width):
    result1 = [string[i:i + max_width] for i in range(0, len(string), max_width)]
    result = '\n'.join(result1)
    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
