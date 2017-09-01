#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用递归函数移动汉诺塔:
# 3个柱子A,B,C中第一个柱子A的盘子数量为n，
# 打印出把所有盘子从A借助B移动到C的方法：
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')