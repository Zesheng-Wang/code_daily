def count_letter(letter, word_list):
    w = []
    for word in word_list:
        for i in word:
            w.append(i)
    return w.count(letter)


word_list = ['hhhh', 'abcdeh']
letter = input("要统计数量的字母: ")
letter_count = count_letter(letter, word_list)
print("合计 :", letter_count, " 个字母 " + letter)