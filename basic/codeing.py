#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 中文编码utf-8
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
#浮点 保留一位小数
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
r = 85/72 - 1
print('%.1f %%' % r)      #0.2%
#补零
print('%2d-%02d' % (3, 1))    # 3-01
#长度
len1 = len(b'ABC')   #3
print(len1)
len2 = len(b'\xe4\xb8\xad\xe6\x96\x87')   #6
print(len2)
len3 = len('中文'.encode('utf-8'))    #6
print(len3)