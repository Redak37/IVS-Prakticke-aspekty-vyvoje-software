"""!@package docstring
    Project name: Calculator
    File: deviation.py
    Date: 19.04.2020
    Last change: 29.04.2020
    Authors: Jan Juda, Radek Duchoň, Markéta Nedělová
    Licence: GNU GPLv2

    Description: File contains script for calculation selective standard deviation from set of values.


    @file deviation.py

    @brief File contains script for calculation selective standard deviation from set of values
    @authors Jan Juda, Radek Duchoň, Markéta Nedělová

"""

import sys
from src.mathlib import MathLib as m

if __name__ == "__main__":
    """! Main function for profiling task.
    Reads lines from standard input, splits each line by whitespaces and parses the given values.
    Calculates standard deviation from parsed values and prints it on standard output.
    If there are no values on standard input, zero is returned.
    @pre there are only valid number on the standard input and they are separated by whitespaces
    """
    N = 0
    x_sum = 0
    x_square_sum = 0

    for line in sys.stdin:
        for number_str in line.split():
            N = m.add(N, 1)
            number = float(number_str)
            x_sum = m.add(x_sum, number)
            x_square_sum = m.add(x_square_sum, m.pow(number, 2))

    if N == 0:
        print(0)
    else:
        mean = m.div(x_sum, N)
        # selective standard deviation computation
        print(m.root(m.div(m.sub(x_square_sum, m.mul(N, m.pow(mean, 2))), m.sub(N, 1)), 2))
