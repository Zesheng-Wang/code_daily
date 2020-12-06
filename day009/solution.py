marksheet = []
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet += [[name, score]]
        scorelist += [score]
    # print(marksheet)
    # print(scorelist)
    sec_low_score = sorted(list(set(scorelist)))[1]
    # print(sec_low_score)
    for name, score in marksheet:
        if score == sec_low_score:
            print(name)