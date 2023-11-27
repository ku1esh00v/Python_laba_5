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
        tekushee_slagaemoe = 1
        k = 0

        while abs(tekushee_slagaemoe) > EPS:
            tekushee_slagaemoe = ((x / 2) ** (2 * k + n)) / (math.factorial(k) * math.factorial(k + n))
            result += tekushee_slagaemoe
            k += 1

        bessel_value = result
        print("The value of the Bessel function of the first kind:", bessel_value)
