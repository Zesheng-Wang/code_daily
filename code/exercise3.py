# -*- coding: utf-8 -*-
# 函数判断是否是闰年

def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
        leap = True
    return leap


year = int(input())
print(is_leap(year))
