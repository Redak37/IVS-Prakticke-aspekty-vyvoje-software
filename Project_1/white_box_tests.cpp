//======== Copyright (c) 2020, FIT VUT Brno, All rights reserved. ============//
//
// Purpose:     White Box - Tests suite
//
// $NoKeywords: $ivs_project_1 $white_box_code.cpp
// $Author:     Radek Duchon <xducho07@stud.fit.vutbr.cz>
// $Date:       $2020-03-04
//============================================================================//
/**
 * @file white_box_tests.cpp
 * @author Radek Duchon
 * 
 * @brief Implementace testu prace s maticemi.
 */

#include "gtest/gtest.h"
#include "white_box_code.h"

//============================================================================//
// ** ZDE DOPLNTE TESTY **
//
// Zde doplnte testy operaci nad maticemi. Cilem testovani je:
// 1. Dosahnout maximalniho pokryti kodu (white_box_code.cpp) testy.
// 2. Overit spravne chovani operaci nad maticemi v zavislosti na rozmerech 
//    matic.
//============================================================================//


class MatrixTest : public ::testing::Test
{
    protected:
        Matrix m1x1;
        Matrix m1x2;
        Matrix m2x1;
        Matrix m2x2;
        Matrix m2x3;
        Matrix m3x2;
        Matrix m3x3;
        Matrix m6x6;
        Matrix m1x1_2;
        Matrix m2x3_2;
        Matrix m6x6_2;

        virtual void SetUp() {
            m1x1 = Matrix();
            m1x2 = Matrix(1, 2);
            m2x1 = Matrix(2, 1);
            m2x2 = Matrix(2, 2);
            m2x3 = Matrix(2, 3);
            m3x2 = Matrix(3, 2);
            m3x3 = Matrix(3, 3);
            m6x6 = Matrix(6, 6);
            m1x1_2 = Matrix();
            m2x3_2 = Matrix(2, 3);
            m6x6_2 = Matrix(6, 6);
        }
};

//Rozmery matic musi byt kladne
TEST_F(MatrixTest, InvalidConstruct) {
    EXPECT_ANY_THROW(Matrix(-1, 1));
    EXPECT_ANY_THROW(Matrix(0, 0));
    EXPECT_ANY_THROW(Matrix(1, 0));
    EXPECT_ANY_THROW(Matrix(0, 1));
}

//Zkouska ruznych rozmeru a konstruktoru
TEST_F(MatrixTest, ValidConstruct) {
    Matrix *m = new Matrix();
    EXPECT_NO_THROW(delete m);

    EXPECT_NO_THROW(Matrix());
    EXPECT_NO_THROW(Matrix(1, 1));
    EXPECT_NO_THROW(Matrix(1, 10));
    EXPECT_NO_THROW(Matrix(10, 1));
    EXPECT_NO_THROW(Matrix(10, 10));
}

//Ziskani hodnoty
TEST_F(MatrixTest, ValidGetValue) {
    EXPECT_TRUE(Matrix().get(0, 0) == 0);
    EXPECT_TRUE(Matrix(1, 1).get(0, 0) == 0);
    EXPECT_TRUE(m1x2.get(0, 1) == 0);
}

//Snaha ziskat neplatnou hodnotu
TEST_F(MatrixTest, InvalidGetValue) {
    EXPECT_ANY_THROW(Matrix().get(0, 1));
    EXPECT_ANY_THROW(Matrix().get(-1, 0));
    EXPECT_ANY_THROW(Matrix(1, 1).get(-1, 0));
    EXPECT_ANY_THROW(m1x2.get(1, 0));
    EXPECT_ANY_THROW(m1x2.get(0, 2));
}

//Nastaveni hodnot
TEST_F(MatrixTest, ValidSetValue) {
    EXPECT_TRUE(m1x1.set(0, 0, 1));
    EXPECT_TRUE(m1x1.get(0, 0) == 1);
    EXPECT_TRUE(m1x2.set(0, 0, 1));
    EXPECT_TRUE(m1x2.set(0, 1, 1));
    EXPECT_TRUE(m6x6.set(0, 5, 1));
}

//Neplatne nastaveni hodnoty
TEST_F(MatrixTest, InvalidSetValue) {
    EXPECT_FALSE(m1x1.set(0, 1, 1));
    EXPECT_TRUE(m1x1.get(0, 0) == 0);
}

//Nastaveni hodnot
TEST_F(MatrixTest, ValidSetValues) {
    EXPECT_TRUE(m1x1.set({{1}}));
    EXPECT_TRUE(m2x2.set({{1, 2}, {3, 4}}));
    EXPECT_TRUE(m1x1.get(0, 0) == 1);
    EXPECT_TRUE(m2x2.get(0, 0) == 1);
    EXPECT_TRUE(m2x2.get(0, 1) == 2);
    EXPECT_TRUE(m2x2.get(1, 0) == 3);
    EXPECT_TRUE(m2x2.get(1, 1) == 4);
}

//Neplatne nastavnei hodnot
TEST_F(MatrixTest, InvalidSetValues) {
    EXPECT_FALSE(m1x1.set({{2, 3}}));
    EXPECT_TRUE(m1x1.get(0, 0) == 0);

    EXPECT_FALSE(m1x1.set({{2}, {3}}));
    EXPECT_TRUE(m1x1.get(0, 0) == 0);
}

//Zkouska rovnosti
TEST_F(MatrixTest, Equal) {
    EXPECT_TRUE(m1x1 == m1x1);
    EXPECT_TRUE(m1x2 == m1x2);
    EXPECT_TRUE(m2x3 == m2x3);
    EXPECT_TRUE(m3x2 == m3x2);
    EXPECT_TRUE(m6x6 == m6x6);
}

//Vyjimka pri nestejne velkych matisich pro rovnost
TEST_F(MatrixTest, NotEqualThrow) {
    EXPECT_ANY_THROW(m1x1 == m1x2);
    EXPECT_ANY_THROW(m1x2 == m3x2);
    EXPECT_ANY_THROW(m2x3 == m3x2);
    EXPECT_ANY_THROW(m3x2 == m6x6);
    EXPECT_ANY_THROW(m6x6 == m1x1);
}

//Nerovnost matic
TEST_F(MatrixTest, NotEqual) {
    m1x1.set({{1}});
    m2x3.set({{1, 2, 3}, {1, 2, 3}});
    m2x3_2.set({{3, 2, 1}, {1, 2, 3}});
    m6x6.set(0, 0, 1);

    EXPECT_FALSE(m1x1 == m1x1_2);
    EXPECT_FALSE(m2x3 == m2x3_2);
    EXPECT_FALSE(m6x6 == m6x6_2);
}

//Scitani matic
TEST_F(MatrixTest, Plus) {
    EXPECT_TRUE(m1x1 + m1x1 == m1x1_2);
    EXPECT_TRUE(m1x2 + m1x2 == m1x2);
    EXPECT_TRUE(m2x3 + m2x3 == m2x3_2);
    EXPECT_TRUE(m3x2 + m3x2 == m3x2);
    EXPECT_TRUE(m6x6 + m6x6 == m6x6_2);

    m1x1.set({{1}});
    m1x1_2.set({{2}});
    m2x3.set({{1, -2, 3}, {-1, 2, -3}});
    m2x3_2.set({{2, -4, 6}, {-2, 4, -6}});
    EXPECT_TRUE(m1x1 + m1x1 == m1x1_2);
    EXPECT_TRUE(m2x3 + m2x3 == m2x3_2);
}

//Vyjimka pri scitani
TEST_F(MatrixTest, PlusThrow) {
    EXPECT_ANY_THROW(m1x1 + m1x2);
    EXPECT_ANY_THROW(m1x2 + m3x2);
    EXPECT_ANY_THROW(m2x3 + m3x2);
    EXPECT_ANY_THROW(m3x2 + m6x6);
    EXPECT_ANY_THROW(m6x6 + m1x1);
}

//Nasobeni matic
TEST_F(MatrixTest, MatrixMultiplication) {
    EXPECT_TRUE(m1x1 * m1x1 == m1x1_2);
    EXPECT_TRUE(m1x2 * m2x1 == m1x1);
    EXPECT_TRUE(m2x3 * m3x2 == m2x2);
    EXPECT_TRUE(m3x2 * m2x3 == m3x3);
    EXPECT_TRUE(m6x6 * m6x6 == m6x6_2);
}

//Vyjimka pri nasobeni matic
TEST_F(MatrixTest, MatrixMultiplicationThrow) {
    EXPECT_ANY_THROW(m1x2 * m1x1);
    EXPECT_ANY_THROW(m1x2 * m3x2);
    EXPECT_ANY_THROW(m1x2 * m1x2);
    EXPECT_ANY_THROW(m3x2 * m6x6);
    EXPECT_ANY_THROW(m6x6 * m1x1);
}

//Nasobeni matice konstantou
TEST_F(MatrixTest, Multiplication) {
    EXPECT_TRUE(m1x1 * 987.654321 == m1x1_2);
    EXPECT_TRUE(m1x2 * -0.001 == m1x2);
    EXPECT_TRUE(m2x3 * 3.14159265358979323846 == m2x3);
    EXPECT_TRUE(m3x2 * 0 == m3x2);
    EXPECT_TRUE(m6x6 * 1 == m6x6_2);

    m2x3.set({{1, -2, 3}, {-1, 2, -3}});
    EXPECT_TRUE(m2x3 * 2 == m2x3 + m2x3);
}

//Vyhodnoceni matic
TEST_F(MatrixTest, Equation) {
    m1x1.set({{-5}});
    EXPECT_TRUE(m1x1.solveEquation({0}) == std::vector<double> {0});
    EXPECT_TRUE(m1x1.solveEquation({1})  == std::vector<double> {-0.2});
    m2x2.set({{1, 1}, {1, -1}});
    EXPECT_TRUE(m2x2.solveEquation({1, -1}) == (std::vector<double> {0, 1}));
    m3x3.set({{1, 2, 3}, {2, 6, 8}, {3, 7, 11}});
    EXPECT_TRUE(m3x3.solveEquation({1, -2, 3}) == (std::vector<double> {3, -4, 2}));
    m6x6.set({{1, 0, 0, 0, 0, 0},
              {1, 1, 0, 0, 0, 0},
              {1, 0, 1, 0, 0, 0},
              {1, 0, 0, 1, 0, 0},
              {1, 0, 0, 0, 1, 0},
              {1, 1, 1, 1, 1, 1}});
    EXPECT_TRUE(m6x6.solveEquation({1, 2, 3, 4, 5, 6}) == (std::vector<double> {1, 1, 2, 3, 4, -5}));
}

//Vyhodnoceni matic vyjimky
TEST_F(MatrixTest, EquationThrow) {
    EXPECT_ANY_THROW(m1x2.solveEquation({1}));
    EXPECT_ANY_THROW(m2x1.solveEquation({1}));
    EXPECT_ANY_THROW(m1x1.solveEquation({1, 1}));
    EXPECT_ANY_THROW(m1x1.solveEquation({1}));
    EXPECT_ANY_THROW(m1x1.solveEquation({0}));
    EXPECT_ANY_THROW(m6x6.solveEquation({1, 2, 3, 4, 5, 6}));
    m6x6.set({{1, 0, 0, 0, 0, 0},
              {1, 1, 0, 0, 0, 0},
              {1, 1, 1, 0, 0, 0},
              {1, 1, 1, 1, 0, 0},
              {0, 0, 0, 0, 1, 1},
              {1, 1, 1, 1, 1, 1}});
    EXPECT_ANY_THROW(m6x6.solveEquation({1, 2, 3, 4, 5, 6}));
}

/*** Konec souboru white_box_tests.cpp ***/
