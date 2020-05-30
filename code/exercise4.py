if __name__ == '__main__':

    list1 = []

    for i in range(int(input())):
        str1 = input()
        list1.append(str1)
    for word in list1:
        stra = word[::2]  # 切片思想，从下标为0开始切出偶数下标的字符串
        strb = word[1::2]  # 切片思想，从下标为1开始切出奇数下标的字符串
        print(stra + ' ' + strb)