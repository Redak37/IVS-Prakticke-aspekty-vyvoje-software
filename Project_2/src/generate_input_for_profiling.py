"""!@package docstring
    Project name: Calculator
    File: generate_input_for_profiling.py
    Date: 19.04.2020
    Last change: 19.04.2020
    Authors: Jan Juda, Radek Duchoň, Markéta Nedělová

    Description: This file generates input files for profiling.


    @file generate_input_for_profiling.py

    @brief This file generates input files for profiling.
    @authors Jan Juda, Radek Duchoň, Markéta Nedělová

"""

from random import uniform


def generateNumbers(filename, N):
    """! Function generates N number of random numbers from interval 0 to 1000 with uniform distribution and saves them
    to a file, one number per line.
    @param filename: name of file to save generated numbers to
    @param N: number of values to generate
    """
    f = open(filename, "w")
    for i in range(0, N):
        f.write(str(uniform(0, 1000)) + "\n")
    f.close()


if __name__ == "__main__":
    """ Entry point for generating input files from assignment. """
    generateNumbers("input10.txt", 10)
    generateNumbers("input100.txt", 100)
    generateNumbers("input1000.txt", 1000)
    # generateNumbers("input10000000.txt", 10000000)

