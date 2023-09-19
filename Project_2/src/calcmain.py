#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""!@package docstring
    Project name: Calculator
    File: calcmain.py
    Date: 19.04.2020
    Last change: 29.04.2020
    Licence: GNU GPLv2
    Authors: Jan Juda, Radek Duchoň, Markéta Nedělová

    Description: This is a main file. It contains GUI controller for our calculator.


    @file calcmain.py

    @brief This is a main file. It contains GUI controller for our calculator.
    @authors Jan Juda, Radek Duchoň, Markéta Nedělová

"""

import numbers
import sys
from os.path import realpath, dirname
from mathlib import MathLib as m
from PyQt5 import QtWidgets, QtGui
from calc import Ui_MainWindow


class Controller:
    """! class that controls GUI """

    """! variable - list of supported operators"""
    operators = ["+", "-", "*", "/", "√", "^", "!", "%"]

    def __init__(self, window):
        """! constructor of class that makes connection between the buttons and actions
        @param window: main application QMainWindow
        """

        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)
        # Connections between buttons and actions
        self.ui.btn_0.clicked.connect(lambda: self.displayWrite("0"))
        self.ui.btn_1.clicked.connect(lambda: self.displayWrite("1"))
        self.ui.btn_2.clicked.connect(lambda: self.displayWrite("2"))
        self.ui.btn_3.clicked.connect(lambda: self.displayWrite("3"))
        self.ui.btn_4.clicked.connect(lambda: self.displayWrite("4"))
        self.ui.btn_5.clicked.connect(lambda: self.displayWrite("5"))
        self.ui.btn_6.clicked.connect(lambda: self.displayWrite("6"))
        self.ui.btn_7.clicked.connect(lambda: self.displayWrite("7"))
        self.ui.btn_8.clicked.connect(lambda: self.displayWrite("8"))
        self.ui.btn_9.clicked.connect(lambda: self.displayWrite("9"))
        self.ui.btn_dot.clicked.connect(lambda: self.displayWrite("."))
        self.ui.btn_add.clicked.connect(lambda: self.displayWrite("+"))
        self.ui.btn_sub.clicked.connect(lambda: self.displayWrite("-"))
        self.ui.btn_mul.clicked.connect(lambda: self.displayWrite("*"))
        self.ui.btn_div.clicked.connect(lambda: self.displayWrite("/"))
        self.ui.btn_mod.clicked.connect(lambda: self.displayWrite("%"))
        self.ui.btn_root.clicked.connect(lambda: self.displayWrite("√"))
        self.ui.btn_pow.clicked.connect(lambda: self.displayWrite("^"))
        self.ui.btn_fact.clicked.connect(lambda: self.displayWrite("!"))
        self.ui.btn_bracket_start.clicked.connect(lambda: self.displayWrite("("))
        self.ui.btn_bracket_end.clicked.connect(lambda: self.displayWrite(")"))
        self.ui.btn_erase.clicked.connect(self.erase)
        self.ui.btn_clear.clicked.connect(lambda: self.ui.display.setText(""))
        self.ui.btn_result.clicked.connect(self.solve)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionHow_this_works.triggered.connect(self.help)

    def displayWrite(self, char):
        """! This function writes text on the display and defines rules for it
        @param char character to be written on display
        """
        
        text = self.ui.display.text()

        # Clear the display when there is an error
        if text == "ERROR":
            text = ""
        first_space = "" if len(text) > 0 and text[-1] == " " else " "
        # Adjust the appearance of the text on the display
        if char in self.operators:
            if len(text) > 0 and text[-1] == " ":
                if len(text) > 3 or char == "-":
                    if text[-2] == ')':
                        self.ui.display.setText(text + first_space + char + " ")
                    elif text[-2] != "(":
                        if text[-2] == "!":
                            self.ui.display.setText(text + char + " ")
                        elif len(text) < 4 or text[-4] != '(':
                            self.ui.display.setText(text[0:-2] + char + " ")
                    elif char == "-":
                        if text[-2] == '(':
                            self.ui.display.setText(text + first_space + char)
                        else:
                            self.ui.display.setText(text + first_space + char + " ")
            elif len(text) > 0 and text[-1] != "-":
                self.ui.display.setText(text + first_space + char + " ")
            elif char == "-":
                self.ui.display.setText(text + char)
        elif char == ")":
            if text.count("(") > text.count(")") and text[-2] != '(' and text[-1] != "-" and\
                    (text[-2] not in self.operators or text[-1] != " " or text[-2] == "!"):
                self.ui.display.setText(text + first_space + char + " ")
        elif char == "(":
            if len(text) == 0 or (len(text) >= 2 and text[-2] in self.operators and text[-2] != "!"):
                self.ui.display.setText(text + first_space + char + " ")
        elif len(text) < 2 or text[-2] != "!":
            self.ui.display.setText(text + char)

    def erase(self):
        """! This function deletes last written character on the display, with it's spaces. """

        text = self.ui.display.text()
        deleteSpace = False
        if len(text) > 0 and text[-1] == " ":
            # Set the characters from position 0 to penultimate position
            text = text[0:-1]
            deleteSpace = True
        text = text[0:-1]
        if len(text) > 0 and text[-1] == " " and deleteSpace:
            text = text[0:-1]
        self.ui.display.setText(text)

    def solve(self):
        """! Solves formula on display using mathematical library. Result is shown on the display. """

        try:
            solved = m.solve(self.ui.display.text())
            if not isinstance(solved, numbers.Number):
                # A result is not a number
                solved = "ERROR"
        except Exception:
            solved = "ERROR"

        self.ui.display.setText(str(solved))

    @staticmethod
    def about():
        """! Gives info about application """

        dialog = QtWidgets.QMessageBox()
        dialog.setIcon(QtWidgets.QMessageBox.Information)
        dialog.setStandardButtons(QtWidgets.QMessageBox.Close)
        dialog.setWindowTitle("About application")
        dialog.setText("RedakGang\'s Calculator v 0.1")
        dialog.setInformativeText("This is calculator application.\n"
                                  "It can perform some basic math.\n"
                                  "Authors: Radek Duchoň, Jan Juda and Markéta Nedělová\n"
                                  "License: GNU GPLv2\n"
                                  "Copyright (c) 2020 Jan Juda, Radek Duchoň and Markéta Nedělová")
        dialog.adjustSize()
        dialog.exec_()

    @staticmethod
    def help():
        """! Gives help about usage of application to user """

        dialog = QtWidgets.QMessageBox()
        dialog.setIcon(QtWidgets.QMessageBox.Information)
        dialog.setStandardButtons(QtWidgets.QMessageBox.Close)
        dialog.setWindowTitle("How this works?")
        dialog.setText("How to use RedakGang's Calculator?")
        dialog.setInformativeText("You can write math formulas using shown buttons,\n"
                                  "and then press '=' button to see the result.\n"
                                  "Application supports \"Scientific mode\" so you can type long formulas\n"
                                  "such as '5 * (3 + 6) / 15'.\n"
                                  "\n"
                                  "Calculator supports KEYBOARD SHORTCUTS!\n"
                                  "So you can use keyboard instead of clicking with mouse!\n"
                                  "\n"
                                  "If you see text 'ERROR' it means, that you have entered incorrect formula.\n"
                                  "You can fix it by just starting to type new formula.\n"
                                  "\n"
                                  "Calculator supports:\n"
                                  " - basic math operators + - * /\n"
                                  " - integer and float numbers\n"
                                  " - brackets\n"
                                  " - factorial (symbol !)\n"
                                  " - modulo (symbol mod)\n"
                                  " - general root (symbol √), number before symbol √ is root degree, "
                                  "so for square root of 25 type '2 √ 25'\n"
                                  " - power (symbol x^n), second number is power degree and "
                                  "it must be a natural integer\n"
                                  "\n"
                                  "Reason for getting an 'ERROR' may be:\n"
                                  " - incorrect usage of brackets, there must be equal "
                                  "number of start and end brackets\n"
                                  " - division (or modulo) by zero\n"
                                  " - using operators on incorrect numbers (such as factorial on a float or power with"
                                  "float degree.\n"
                                  "\n"
                                  "If application \"freezes\" then you have probably typed some long time-"
                                  "consuming formula.\n"
                                  "For example factorial of number greater than 50000 or power/root with high degree.\n"
                                  "If this happens, you can simply wait for the computation to finish or "
                                  "kill the application.")
        dialog.adjustSize()
        dialog.exec_()


if __name__ == "__main__":
    """! Main function. This is application entry point. """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon(dirname(realpath(__file__)) + '/calcmain-icon.png'))
    controller = Controller(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

