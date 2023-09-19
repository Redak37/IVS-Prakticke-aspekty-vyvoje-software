//======== Copyright (c) 2017, FIT VUT Brno, All rights reserved. ============//
//
// Purpose:     Test Driven Development - priority queue code
//
// $NoKeywords: $ivs_project_1 $tdd_code.cpp
// $Author:     Radek Duchon <xducho07@stud.fit.vutbr.cz>
// $Date:       $2020-03-03
//============================================================================//
/**
 * @file tdd_code.cpp
 * @author Radek Duchon
 * 
 * @brief Implementace metod tridy prioritni fronty.
 */

#include <stdlib.h>
#include <stdio.h>

#include "tdd_code.h"

//============================================================================//
// ** ZDE DOPLNTE IMPLEMENTACI **
//
// Zde doplnte implementaci verejneho rozhrani prioritni fronty (Priority Queue)
// 1. Verejne rozhrani fronty specifikovane v: tdd_code.h (sekce "public:")
//    - Konstruktor (PriorityQueue()), Destruktor (~PriorityQueue())
//    - Metody Insert/Remove/Find a GetHead
//    - Pripadne vase metody definovane v tdd_code.h (sekce "protected:")
//
// Cilem je dosahnout plne funkcni implementace prioritni fronty implementovane
// pomoci tzv. "double-linked list", ktera bude splnovat dodane testy 
// (tdd_tests.cpp).
//============================================================================//

//Inicializuje prazdny seznam
PriorityQueue::PriorityQueue()
{
    head = NULL;
}

//Zrusi seznam
PriorityQueue::~PriorityQueue()
{
    Element_t *item, *item2 = GetHead();
    while (item2) {
        item = item2;
        item2 = item2->pNext;
        delete item;
    }
}

//Vlozi hodnotu do seznamu
void PriorityQueue::Insert(int value)
{
    Element_t *newItem = new Element_t;

    Element_t *item = GetHead();
    //pokud je nova polozka prvni nebo nejmensi, vlozit na prvni misto
    if (!item || item->value >= value) {
        *newItem = {head, NULL, value};

        if (head)
            head->pPrev = newItem;

        head = newItem;
        return;
    }
    //Hleda misto ke vlozeni
    while (item->pNext && item->pNext->value < value) {
        item = item->pNext;
    }

    *newItem = {item->pNext, item, value};

    if (item->pNext)
        item->pNext->pPrev = newItem;

    item->pNext = newItem;
}

//Odstrani prvni polozku zadane hodnoty
bool PriorityQueue::Remove(int value)
{
    if (Element_t *item = Find(value)) {
        //Spojeni zbytku seznamu
        if (item->pPrev) {
            item->pPrev->pNext = item->pNext;
        } else
            head = item->pNext;

        if (item->pNext)
            item->pNext->pPrev = item->pPrev;

        delete item;

        return true;
    }
    return false;
}

//Najde prvni polozku zadane hodnoty v seznamu
PriorityQueue::Element_t *PriorityQueue::Find(int value)
{
    for (Element_t *item = GetHead(); item != NULL; item = item->pNext) {
        if (item->value == value)
            return item;
    }

    return NULL;
}

//Vrati ukazatel na zacatek seznamu
PriorityQueue::Element_t *PriorityQueue::GetHead()
{
    return head;
}

/*** Konec souboru tdd_code.cpp ***/
