if __name__ == '__main__':
    # first method ：use set
    num_list = list(map(int, input().split()))

    num_list = list(set(num_list))
    max_num = max(num_list)
    num_list.remove(max_num)
    sec_max = max(num_list)
    print(sec_max)

    # second method : use while
    i = int(input())
    lis = list(map(int, input().strip().split()))
    print(lis)
    z = max(lis)
    while max(lis) == z:
        lis.remove(max(lis))

    print(max(lis))