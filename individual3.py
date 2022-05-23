#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print("введите продложение\n")
    print(''.join(char for i, char in enumerate(
        input()) if not (char == 'о' and i % 2 == 0)))