"""
Radix Sort
"""

def radix_sort(lst, n, maxLen):
  for x in xrange(maxLen):
    bins = [[] for i in xrange(n)]
    for y in lst:
      bins[(y/10**x)%n].append(y)
    lst = sum(bins, [])
  return lst
