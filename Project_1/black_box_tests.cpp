//======== Copyright (c) 2020, FIT VUT Brno, All rights reserved. ============//
//
// Purpose:     Red-Black Tree - public interface tests
//
// $NoKeywords: $ivs_project_1 $black_box_tests.cpp
// $Author:     Radek Dcuhon <xducho07@stud.fit.vutbr.cz>
// $Date:       $2020-03-02
//============================================================================//
/**
 * @file black_box_tests.cpp
 * @author Radek Duchon
 * 
 * @brief Implementace testu binarniho stromu.
 */

#include <vector>

#include "gtest/gtest.h"

#include "red_black_tree.h"

//============================================================================//
// ** ZDE DOPLNTE TESTY **
//
// Zde doplnte testy Red-Black Tree, testujte nasledujici:
// 1. Verejne rozhrani stromu
//    - InsertNode/DeleteNode a FindNode
//    - Chovani techto metod testuje pro prazdny i neprazdny strom.
// 2. Axiomy (tedy vzdy platne vlastnosti) Red-Black Tree:
//    - Vsechny listove uzly stromu jsou *VZDY* cerne.
//    - Kazdy cerveny uzel muze mit *POUZE* cerne potomky.
//    - Vsechny cesty od kazdeho listoveho uzlu ke koreni stromu obsahuji
//      *STEJNY* pocet cernych uzlu.
//============================================================================//

class EmptyTree : public ::testing::Test
{
    protected:
        BinaryTree tree;
};

class NonEmptyTree : public ::testing::Test
{
    protected:
        BinaryTree tree;

        virtual void SetUp() {
            int values[] = { 10, 85, 15, 70, 20, 60, 30, 50, 65, 80, 90, 40, 5, 55 };
            for (int value : values)
                tree.InsertNode(value);
        }
};

class TreeAxioms : public ::testing::Test
{
    protected:
        BinaryTree tree;

        virtual void SetUp() {
            int values[] = { 10, 85, 15, 70, 20, 60, 30, 50, 65, 80, 90, 40, 5, 55 };
            for (int value : values)
                tree.InsertNode(value);
        }
};

//Test vlozeni uzlu do neprazdneho stromu
TEST_F(EmptyTree, InsertNode) {
    std::pair<bool, BinaryTree::Node_t *> pair = tree.InsertNode(0);
    EXPECT_TRUE(pair.first);
    EXPECT_TRUE(pair.second != NULL);
}

//Test vlozeni uzlu do prazdneho stromu
TEST_F(NonEmptyTree, InsertNode) {
    std::pair<bool, BinaryTree::Node_t *> pair = tree.InsertNode(0);
    EXPECT_TRUE(pair.first);
    EXPECT_TRUE(pair.second != NULL);
    
    pair = tree.InsertNode(0);
    EXPECT_FALSE(pair.first);
    EXPECT_TRUE(pair.second != NULL);
}

//Test smazani neexistujiciho uzlu
TEST_F(EmptyTree, DeleteNode) {
    EXPECT_FALSE(tree.DeleteNode(0));
}

//Test smazani uzlu z neprazdneho stromu
TEST_F(NonEmptyTree, DeleteNode) {
    EXPECT_TRUE(tree.DeleteNode(10));
    EXPECT_FALSE(tree.DeleteNode(10));
    tree.InsertNode(10);
    EXPECT_TRUE(tree.DeleteNode(10));
}

//Test vyhledavani uzlu
TEST_F(EmptyTree, FindNode) {
    EXPECT_TRUE(tree.FindNode(0) == NULL);
}

//Test vyhledavani uzlu v neprazdnem stromu
TEST_F(NonEmptyTree, FindNode) {
    EXPECT_TRUE(tree.FindNode(0) == NULL);
    Node_t *node = tree.FindNode(10);
    EXPECT_TRUE(node != NULL);
    EXPECT_TRUE(node->key == 10);
}

//Prazdny strom nema listy
TEST_F(EmptyTree, NoLeafNodes) {
    std::vector<BinaryTree::Node_t*> leafNodes;
    tree.GetLeafNodes(leafNodes);
    EXPECT_TRUE(leafNodes.empty());
}

//Listy stromu jsou cerne a nemaji potomky
TEST_F(TreeAxioms, Axiom1) {
    std::vector<BinaryTree::Node_t*> leafNodes;
    tree.GetLeafNodes(leafNodes);
    ASSERT_FALSE(leafNodes.empty());

    for (Node_t* node : leafNodes) {
        EXPECT_TRUE(node->pLeft == NULL);
        EXPECT_TRUE(node->pRight == NULL);
        EXPECT_TRUE(node->color == BLACK);
    }
}

//Cervene uzly maji cerne potomky, Listy mohou byt nil
TEST_F(TreeAxioms, Axiom2) {
    std::vector<BinaryTree::Node_t*> leafNodes;
    tree.GetNonLeafNodes(leafNodes);
    ASSERT_FALSE(leafNodes.empty());

    for (Node_t* node : leafNodes) {
        if (node->color == RED) {
            EXPECT_TRUE(node->pLeft == NULL || node->pLeft->color == BLACK);
            EXPECT_TRUE(node->pRight == NULL || node->pRight->color == BLACK);
        }
    }
}

//Ode vsech uzlu vede k rootu stejne cernych uzlu
TEST_F(TreeAxioms, Axiom3) {
    std::vector<BinaryTree::Node_t*> leafNodes;
    tree.GetLeafNodes(leafNodes);
    ASSERT_FALSE(leafNodes.empty());

    int black = -1;
    for (Node_t* node : leafNodes) {
        int act = 0;
        while (node->pParent != NULL) {
            node = node->pParent;
            if (node->color == BLACK)
                act++;
        }
        if (black == -1)
            black = act;
        else
            EXPECT_TRUE(black == act);
    }
}

/*** Konec souboru black_box_tests.cpp ***/
