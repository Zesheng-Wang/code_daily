def swap_case(s):
    # first method
    b = []
    for n in s:
        if "a" <= n <= "z":
            b.append(n.upper())
        elif "A" <= n <= "Z":
            b.append(n.lower())
        else:
            b.append(n)
    return "".join(b)

    # second method
    # return s.swapcase()  # 字符串方法


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
