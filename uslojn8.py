#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s1 = input("введите 1 слово ")
    s2 = input("введите 2 слово ")
    s = s1 + s2
    ls = []
    for c in s:
        if s.count(c) == 1:
            ls.append(c)
    print(ls)