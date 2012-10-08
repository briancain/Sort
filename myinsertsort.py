"""
InsertionSort
Programmed by: Brian Cain
Based off the algorithm from: Introduction to Algorithms by Cormen
"""

import sys

def insertionsort(lst):
    for ri in range(1, len(lst)):
        key = lst[ri]
        i = ri - 1
        while i > 0 and lst[i-1] > key:
            lst[i] = lst[i-1]
            i = i - 1
        lst[i] = key

    return lst
