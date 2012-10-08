"""
Quick Sort
Programmed by: Brian Cain
Based off the algorithm from: 9th Draft Dr Howell
"""

import sys
import math

def quicksort(lst):
    if len(lst) == 0:
        return []
    else:
        p = lst[0]
        low = quicksort([x for x in lst[1:] if x < p])
        high = quicksort([x for x in lst[1:] if x >= p])
        return low + [p] + high
