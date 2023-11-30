#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import *

if __name__ == '__main__':
    a = float(input('Enter the coefficient "a": '))
    b = float(input('Enter the coefficient "b": '))
    c = float(input('Enter the coefficient "c": '))

    if a == 0:
        print('The equation is not biquadrate.')
    else:
        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            print('The equation has no real roots.')
        else:
            t_1 = (-b + sqrt(discriminant)) / (2 * a)
            t_2 = (-b - sqrt(discriminant)) / (2 * a)

            if discriminant == 0:
                print('The equation has two matching real roots:')
                x_1 = sqrt(t_1)
                x_2 = -sqrt(t_1)
                print('x_1 =', x_1)
                print('x_2 =', x_2)
            else:
                print('The equation has four real roots:')
                x_1 = sqrt(t_1)
                x_2 = -sqrt(t_1)
                x_3 = sqrt(t_2)
                x_4 = -sqrt(t_2)
                print('x_1 =', x_1)
                print('x_2 =', x_2)
                print('x_3 =', x_3)
                print('x_4 =', x_4)



