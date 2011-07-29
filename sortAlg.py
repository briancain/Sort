"""
This is a sorting algorithm program.
Programmed by: Brian Cain
Version 1.0
"""

import sys
import select
import termios
import tty
import random
# import timeit

# Sorting algorithm files
# Import more algortihms here
import mybubblesort
import myselectionsort
import myradixsort

print sys.argv

def main():
  lst = []
  while True:
    print """Menu
    1.) Generate Random List
    2.) Bubble Sort
    3.) Selection Sort
    4.) Radix Sort
    5.) About Me
    6.) Quit"""
    answer = getkey()

    if "1" in answer:
      lst = generateList()
    elif "2" in answer:
      if lst:
        lst = mybubblesort.Sort(lst)
    elif "3" in answer:
      if lst:
        lst = myselectionsort.selection_sort(lst)
    elif "4" in answer:
      if lst:
        lst = myradixsort.radix_sort(lst, 10, 5)
    elif "5" in answer:
      printAbout()
    elif "6" in answer:
      break

    if not "5" in answer:
      printList(lst)

    
  exit()

def getkey():
  old_settings = termios.tcgetattr(sys.stdin)
  tty.setraw(sys.stdin.fileno())
  select.select([sys.stdin], [], [], 0)
  answer = sys.stdin.read(1)
  termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
  return answer

def printList(lst):
  print "================="
  print "Our current list:"
  print lst
  print "\n"

def printAbout():
  f = open('about.txt', 'r')
  print "================="
  for line in f:
    print line
  
  f.close()

def generateList():
  print "Generating list..."
  rng = input("Enter Max Size: ")
  lst = []
  for i in range(rng):
    lst.append(random.randint(1,100))
  return lst

def exit():
  sys.exit()

if __name__ == '__main__':
  main()
