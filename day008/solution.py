if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    champion = max(arr)  # 冠军得分
    arr = list(set(arr))
    arr.remove(champion)
    runner_up = max(arr)  # 亚军得分
    print(runner_up)
