#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""!@package docstring
    Project name: Calculator
    File: tests.py
    Date: 19.04.2020
    Last change: 29.04.2020
    Authors: Jan Juda, Radek Duchoň, Markéta Nedělová
    Licence: GNU GPLv2

    Description: This file contains tests for calculator's mathematical library.


    @file tests.py

    @brief This file contains tests for calculator's mathematical library.
    @authors Jan Juda, Radek Duchoň, Markéta Nedělová

"""

import unittest
from mathlib import MathLib as m


class MathLibTests(unittest.TestCase):
    """! Tests for calculator's mathematical library"""

    def test_add(self):
        """! An addition testing """
        self.assertEqual(5, m.add(2, 3))
        self.assertEqual(0, m.add(0, 0))
        self.assertEqual(-8878555, m.add(-8888555, 10000))
        self.assertEqual(0.5, m.add(0.2, 0.3))
        self.assertEqual(-0.01, m.add(-0.0097, -0.0003))

    def test_sub(self):
        """! A subtraction testing """
        self.assertEqual(15, m.sub(20, 5))
        self.assertEqual(-82, m.sub(8, 90))
        self.assertEqual(-3, m.sub(-3, 0))
        self.assertEqual(-0.25, m.sub(0, 0.25))
        self.assertEqual(0.000864, m.sub(0.000987, 0.000123))

    def test_mul(self):
        """! A multiplication testing """
        self.assertEqual(24, m.mul(4, 6))
        self.assertEqual(-25, m.mul(-5, 5))
        self.assertEqual(48, m.mul(-6, -8))
        self.assertEqual(-4, m.mul(8, -0.5))
        self.assertEqual(1250, m.mul(1000000, 0.00125))
        self.assertEqual(1.1, m.mul(5.5, 0.2))

    def test_div(self):
        """! A division testing """
        self.assertEqual(4, m.div(8, 2))
        self.assertEqual(-56, m.div(-28, 0.5))
        self.assertEqual(-1000, m.div(3000, -3))
        self.assertEqual(8.125, m.div(52, 6.4))
        self.assertEqual(2, m.div(0.2, 0.1))
        self.assertEqual(0, m.div(0, 586.648626))
        with self.assertRaises(Exception):
            m.div(5, 0)  # Can't divide by zero

    def test_fact(self):
        """! A factorial testing """
        self.assertEqual(120, m.fact(5))
        self.assertEqual(1, m.fact(1))
        self.assertEqual(1, m.fact(0))
        with self.assertRaises(Exception):
            m.fact(-1)  # Not a natural number
        with self.assertRaises(Exception):
            m.fact(-845)  # Not a natural number
        with self.assertRaises(Exception):
            m.fact(2.5)  # Not a natural number

    def test_root(self):
        """! A root testing """
        self.assertEqual(4, m.root(16, 2))
        self.assertEqual(2, m.root(1024, 10))
        self.assertEqual(20, m.root(20, 1))
        self.assertEqual(0.5, m.root(0.25, 2))
        self.assertEqual(0.5, m.root(8, -3))
        with self.assertRaises(Exception):
            m.root(545, 0)

    def test_pow(self):
        """! A power testing """
        self.assertEqual(25, m.pow(5, 2))
        self.assertEqual(6654564.3565, m.pow(6654564.3565, 1))
        self.assertEqual(1, m.pow(864654.23265, 0))
        self.assertEqual(-0.125, m.pow(-0.5, 3))
        with self.assertRaises(Exception):
            m.pow(123, -2)  # -2 is't natural exponent
        with self.assertRaises(Exception):
            m.pow(456, 1.2)  # 1.2 is float exponent, not natural

    def test_mod(self):
        """! A modulo testing """
        self.assertEqual(1, m.mod(5, 2))
        self.assertEqual(0, m.mod(42, 1))
        self.assertEqual(0, m.mod(6, 6))
        self.assertEqual(0, m.mod(-6, 6))
        self.assertEqual(0, m.mod(88, -8))
        self.assertEqual(-9, m.mod(11, -10))
        self.assertEqual(1.5, m.mod(3.5, 2))
        with self.assertRaises(Exception):
            m.mod(5454, 0)  # Can't divide by zero


if __name__ == '__main__':
    """! Entry point for running tests """
    unittest.main()
