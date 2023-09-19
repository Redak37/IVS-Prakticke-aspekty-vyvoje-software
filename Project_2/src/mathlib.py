#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""!@package docstring
    Project name: Calculator
    File: mathlib.py
    Date: 19.04.2020
    Last change: 29.04.2020
    Authors: Jan Juda, Radek Duchoň, Markéta Nedělová
    Licence: GNU GPLv2

    Description: This file is mathematical library for our application.


    @file mathlib.py

    @brief This file is mathematical library for our application.
    @authors Jan Juda, Radek Duchoň, Markéta Nedělová

"""


class MathLib:
    """! Basic math library """

    """! class variable - Dict with priorities of operators """
    operands = {'=': 0, '+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, '!': 3, '√': 3}

    @staticmethod
    def add(a, b):
        """! This function makes addition

        @param a addend
        @param b addend
        @pre a is number
        @pre b is number
        @return an addition result

        """

        return a + b

    @staticmethod
    def sub(a, b):
        """!  This function makes subtraction

        @param a a minuend
        @param b a subtrahend
        @pre a is number
        @pre b is number
        @return: a subtraction result

        """

        return a - b

    @staticmethod
    def mul(a, b):
        """!  A function for making multiplication

        @param a  a first factor
        @param b  a second factor
        @pre a is number
        @pre b is number
        @return a multiplication result

        """

        return a * b

    @staticmethod
    def div(a, b):
        """!  A function for making division

        @param a  a dividend
        @param b  a divisor
        @pre b is not 0
        @pre a is number
        @pre b is number
        @return a division result

        """

        " Can't divide by zero "
        if b == 0:
            raise ValueError("Exception")

        return a / b

    @staticmethod
    def mod(a, b):
        """! This function makes modulo

        @param a  a dividend
        @param b  a divisor
        @pre b is not 0
        @pre a is number
        @pre b is number
        @return a modulo result

        """

        # Can't divide by zero
        if b == 0:
            raise ValueError("Exception")

        return a % b

    @staticmethod
    def fact(a):
        """! This function makes factorial

        @param a natural number for factorial
        @pre a is natural integer
        @return a factorial result

        """

        if (isinstance(a, float) and not a.is_integer()) or a < 0:
            raise ValueError("Exception")

        result = 1
        for i in range(2, int(a) + 1):
            result *= i

        return result

    @staticmethod
    def root(x, n):
        """! A function for making root

        @param x base root
        @param n an exponent
        @pre n is not 0
        @pre x is number
        @pre n is number
        @return a root result

        """

        # Can't divide by zero
        if n == 0:
            raise ValueError("Exception")

        return x ** (1 / n)

    @staticmethod
    def pow(x, n):
        """! A function for making power

        @param x base power
        @param n an exponent
        @pre x is number
        @pre n is natural integer
        @return a power result

        """

        if (isinstance(n, float) and not n.is_integer()) or n < 0:
            raise ValueError("Exception")

        # Changed after profiling, but it has actually worse timing than the original one
        # result = 1
        # for i in range(0, int(n)):
        #     result *= x
        #
        # return result
        return x ** n

    @staticmethod
    def parse(equation):
        """! A function for parsing
        @param equation string with math problem
        @pre equation is entered correctly and members are separated by space
        @return postfix notation of equation in list
        """

        s = []
        postfix = []
        for x in equation.split():
            if x == ')':
                while s[-1] != '(':
                    postfix.append(s.pop())
                s.pop()
            elif x == '(':
                s.append('(')
            elif x not in MathLib.operands.keys():
                postfix.append(float(x))
            else:
                while not (not len(s) or s[-1] == '(' or MathLib.operands[s[-1]] < MathLib.operands[x]):
                    postfix.append(s.pop())
                s.append(x)

        while len(s):
            postfix.append(s.pop())

        return postfix

    @staticmethod
    def solve(equation):
        """! A function for solving the math problem
        @param equation string with math problem
        @pre equation is entered correctly and members are separated by space
        @return result of equation
        """

        s = [0.0]
        for x in MathLib.parse(equation):
            if x not in MathLib.operands:
                s.append(x)
            else:
                b = s.pop()
                if x == '+':
                    s.append(MathLib.add(s.pop(), b))
                elif x == '-':
                    s.append(MathLib.sub(s.pop(), b))
                elif x == '*':
                    s.append(MathLib.mul(s.pop(), b))
                elif x == '/':
                    s.append(MathLib.div(s.pop(), b))
                elif x == '%':
                    s.append(MathLib.mod(s.pop(), b))
                elif x == '√':
                    s.append(MathLib.root(s.pop(), b))
                elif x == '^':
                    s.append(MathLib.pow(s.pop(), b))
                elif x == '!':
                    s.append(MathLib.fact(b))
                else:
                    raise ValueError("Exception")

        if isinstance(s[-1], float) and s[-1].is_integer():
            return int(s[-1])

        return s[-1]

""" End of file mathlib.py """
