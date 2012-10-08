"""
Merge Sort
Programmed by: Brian Cain
Based off the algorithm from: Introduction to Algorithms by Cormen
"""

import sys
import math

def merge(Left, Right):
    Result = []

    while len(Left) > 0 or len(Right) > 0:
        if len(Left) > 0 and len(Right) > 0:
            if Left[0] <= Right[0]:
                Result.append(Left[0])
                Left = Left[1:]
            else:
                Result.append(Right[0])
                Right = Right[1:]
        elif len(Left) > 0:
            Result.append(Left[0])
            Left = Left[1:]
        elif len(Right) > 0:
            Result.append(Right[0])
            Right = Right[1:]

    return Result

def mergesort(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) / 2
    Left = lst[:middle]
    Right = lst[middle:]

    Left = mergesort(Left)
    Right = mergesort(Right)
    return merge(Left, Right)
