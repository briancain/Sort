"""
Bubble Sort
Programmed by: Brian Cain
"""

import sys

def Sort(lst):
  for passLeft in range(len(lst)-1, 0, -1):
    for i in range(passLeft):
      if lst[i] > lst[i + 1]:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
  return lst
