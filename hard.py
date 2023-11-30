#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

if __name__ == '__main__':
    n = int(input("Enter the value n: "))
    x = float(input("Enter the value of the function argument: "))

    if x == 0:
        print('Недопустимое значение x', file=sys.stderr)
        exit(1)
    else:
        EPS = float(input("Enter the accuracy value: "))
        result = 0
        k = 0
        tekushee_slagaemoe = 1 / math.factorial(n)

        while math.fabs(tekushee_slagaemoe) > EPS:
            tekushee_slagaemoe *= x ** 2 / (4 * (k + n + 1) * (k + 1))
            result += tekushee_slagaemoe
            k += 1

        print(f'I{n}({x}) = {((x / 2) ** n) * result}')
