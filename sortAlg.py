"""
This is a sorting algorithm program.
Programmed by: Brian Cain
Version 2.0
"""

import os
import sys
import select
import termios
import tty
import random
import time
import math
import datetime

# Sorting algorithm files
# Import more algortihms here
import mybubblesort
import myselectionsort
import myradixsort
import myinsertsort
import mymergesort
import myquicksort

print sys.argv

def main():
    lst = []
    while True:
        print """Menu
        1.) Generate Random List
        2.) Generate New Test
        3.) Bubble Sort
        4.) Selection Sort
        5.) Radix Sort
        6.) Insertion Sort
        7.) Merge Sort
        8.) Quick Sort
        9.) Quit"""
        answer = getkey()

        if "1" in answer:
            lst = generateList()
            printList(lst)
        elif "2" in answer:
            generateFile(lst)
        elif "3" in answer:
            if lst:
                print "\nCalculating..."
                start = time.time()
                lst = mybubblesort.Sort(lst)
                elapsed = (time.time() - start)
                printSort(lst, elapsed, "Bubble Sort")
        elif "4" in answer:
            if lst:
                print "\nCalculating..."
                start = time.time()
                lst = myselectionsort.selection_sort(lst)
                elapsed = (time.time() - start)
                printSort(lst, elapsed, "Selection Sort")
        elif "5" in answer:
            if lst:
                print "\nCalculating..."
                start = time.time()
                lst = myradixsort.radix_sort(lst, 10, 5)
                elapsed = (time.time() - start)
                printSort(lst, elapsed, "Radix Sort")
        elif "6" in answer:
            if lst:
                print "\nCalculating..."
                start = time.time()
                lst = myinsertsort.insertionsort(lst)
                elapsed = (time.time() - start)
                printSort(lst, elapsed, "Insertion Sort")
        elif "7" in answer:
            if lst:
                print "\nCalculating..."
                start = time.time()
                lst = mymergesort.mergesort(lst)
                elapsed = (time.time() - start)
                printSort(lst, elapsed, "Merge Sort")
        elif "8" in answer:
            if lst:
                print "\nCalculating..."
                start = time.time()
                lst = myquicksort.quicksort(lst)
                elapsed = (time.time() - start)
                printSort(lst, elapsed, "Quick Sort")
        elif "9" in answer:
            exit()
            # break
        else:
            print "\nPick an option\n"

def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    answer = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    return answer

def printList(lst):
    print "Do you want to print the list [y/n] ?"
    ans = getkey()
    os.system(['clear','cls'][os.name == 'nt'])
    if "y" in ans:
        print "================="
        print "Our current list:"
        print lst
        print "\n"

def printSort(lst, elapsedt, sorttype):
    print "Do you want to print the list [y/n] ?"
    ans = getkey()
    os.system(['clear','cls'][os.name == 'nt'])
    if "y" in ans:
        print "================="
        print "Our current list:"
        print lst
        print "\n"
    print "Elapsed Time ("+ sorttype + "): " + str(elapsedt)

    if sorttype == "Insertion Sort":
        f = open("ins_results.txt", "a")
        f.write("Size of Array: " + str(len(lst)) + "\n")
        f.write("Elapsed Time ("+ sorttype + "): " + str(elapsedt) + " seconds\n")
        f.write("=================\n")
        f.close()
    elif sorttype == "Merge Sort":
        f = open("mge_results.txt", "a")
        f.write("Size of Array: " + str(len(lst)) + "\n")
        f.write("Elapsed Time ("+ sorttype + "): " + str(elapsedt) + " seconds\n")
        f.write("=================\n")
        f.close()
    elif sorttype == "Quick Sort":
        f = open("qck_results.txt", "a")
        f.write("Size of Array: " + str(len(lst)) + "\n")
        f.write("Elapsed Time ("+ sorttype + "): " + str(elapsedt) + " seconds\n")
        f.write("=================\n")
        f.close()
    elif sorttype == "Bubble Sort":
        f = open("bub_results.txt", "a")
        f.write("Size of Array: " + str(len(lst)) + "\n")
        f.write("Elapsed Time ("+ sorttype + "): " + str(elapsedt) + " seconds\n")
        f.write("=================\n")
        f.close()
    elif sorttype == "Selection Sort":
        f = open("sel_results.txt", "a")
        f.write("Size of Array: " + str(len(lst)) + "\n")
        f.write("Elapsed Time ("+ sorttype + "): " + str(elapsedt) + " seconds\n")
        f.write("=================\n")
        f.close()
    elif sorttype == "Radix Sort":
        f = open("rdx_results.txt", "a")
        f.write("Size of Array: " + str(len(lst)) + "\n")
        f.write("Elapsed Time ("+ sorttype + "): " + str(elapsedt) + " seconds\n")
        f.write("=================\n")
        f.close()

def generateFile(lst):
    # get input from user for file name, check if file already exists (or just give an overwrite warning)
    # open file
    # write table to file comparing algorithms

    # elapsed = c * n^2 for insertion, i said that c = elapsed / n^2
    os.system(['clear','cls'][os.name == 'nt'])
    print "Calculating run times and generating file..."
    if len(lst) >= 10000:
        print "Warning, this could take a while...."

    bubblelst = list(lst)
    selectlst = list(lst)
    radixlst = list(lst)
    insertlst = list(lst)
    mergelst = list(lst)
    quicklst = list(lst)

    n = len(lst)

    # Bubble Sort
    start_bubble = time.time()
    lst_bubble = mybubblesort.Sort(bubblelst)
    elapsed_bubble = (time.time() - start_bubble)

    c_bub = elapsed_bubble / ((n^2))

    # Selection Sort
    start_select = time.time()
    lst_select = myselectionsort.selection_sort(lst)
    elapsed_select = (time.time() - start_select)

    c_sel = elapsed_select / ((n^2))

    # Radix Sort
    start_radix = time.time()
    lst_radix = myradixsort.radix_sort(lst, 10, 5)
    elapsed_radix = (time.time() - start_radix)

    # Insertion Sort
    start_insert = time.time()
    lst_insert = myinsertsort.insertionsort(insertlst)
    elapsed_insert = (time.time() - start_insert)

    c_ins = elapsed_insert / ((n^2))

    # Merge Sort
    start_merge = time.time()
    lst_merge = mymergesort.mergesort(mergelst)
    elapsed_merge = (time.time() - start_merge)

    c_merge = elapsed_merge / (n*math.log(n, 2))

    # Quick Sort
    start_quick = time.time()
    lst_quick = myquicksort.quicksort(quicklst)
    elapsed_quick = (time.time() - start_quick)

    c_quick = elapsed_merge / (n*math.log(n, 2))

    now = datetime.datetime.now()
    a = str(now)
    filename = "bccain_cis775_" + a + ".txt"
    f = open(filename, "w")

    f.write("The total size of the list: " + str(len(lst)) + "\n")
    f.write("O(f(n)) |: g(n) <= c*f(n)\n")
    f.write("c = elapsed / <algorith_run_time>\n")
    f.write("========================================\n")
    f.write("Bubble RT O(n^2): " + str(elapsed_bubble) + " seconds.\n")
    f.write("Bubble cb: " + str(c_bub) + "\n\n")
    f.write("Selection RT O(n^2): " + str(elapsed_select) + " seconds.\n")
    f.write("Selection cs: " + str(c_sel) + "\n\n")
    f.write("Radix RT O(kN): " + str(elapsed_radix) + " seconds.\n\n")
    f.write("Insert RT O(n^2): " + str(elapsed_insert) + " seconds.\n")
    f.write("Insert ci: " + str(c_ins) + "\n\n")
    f.write("Merge RT O(nlgn): " + str(elapsed_merge) + " seconds.\n")
    f.write("Merge cm: " + str(c_merge) + "\n\n")
    f.write("Quick RT O(nlgn): " + str(elapsed_quick) + " seconds.\n")
    f.write("Quick cq: " + str(c_quick) + "\n\n")
    f.close()
    print "Written to file name: ", filename

def generateList():
    print "Generating list..."
    rng = input("Enter Max Size: ")
    lst = []
    for i in range(rng):
        lst.append(random.randint(1,1000000))
    return lst

def exit():
    sys.exit()

if __name__ == '__main__':
    main()
