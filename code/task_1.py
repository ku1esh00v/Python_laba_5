#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = int(input('Enter the month number: '))
    if n == 1:
        print('It is January')
    elif n == 2:
        print('It is February')
    elif n == 3:
        print('It is March')
    elif n == 4:
        print('It is April')
    elif n == 5:
        print('It is May')
    elif n == 6:
        print('It is June')
    elif n == 7:
        print('It is July')
    elif n == 8:
        print('It is August')
    elif n == 9:
        print('It is September')
    elif n == 10:
        print('It is October')
    elif n == 11:
        print('It is November')
    elif n == 12:
        print('It is December')
    else:
        print('Ошибка!', file=sys.stderr)
        exit(1)
