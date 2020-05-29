# -*- coding: utf-8 -*-

'''
@Author  : Zesheng Wang
@Time    : 2020/3/7 16:49
@Software: PyCharm
@File    : func_leap_year.py
'''


# 函数判断是否是闰年

def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
        leap = True
    return leap


year = int(input())
print(is_leap(year))
