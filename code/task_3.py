#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print('All two-digit numbers that are divisible by the sum of the digits they consist of:')

    for i in range(10, 100):
        last_digit = i % 10
        first_digit = i // 10

        if i % (last_digit + first_digit) == 0:
            print(i, end =' ',)

