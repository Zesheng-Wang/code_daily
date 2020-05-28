# -*- coding: utf-8 -*-

'''
@Author  : Zesheng Wang
@Time    : 2020/1/12 16:37
@Software: PyCharm
@File    : python_loops.py
'''
'''
Read an integer N. For all non-negative integers i < N, print i**2. See the sample for details.
'''
if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(i ** 2)
