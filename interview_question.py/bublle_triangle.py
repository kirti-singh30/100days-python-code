from unittest.util import sorted_list_difference


def bubble_sort(a):
    b = len(a)-1
    swap = False
    for x in range(b):
        for y in range(b-x):
            if a[y]>a[y+1]:
                swap = True
                a[y],a[y+1] = a[y+1],a[y]

        if not swap:
            exit
    return a
a = [99,56,109,134,23,16]
sorted_list =bubble_sort(a)
print(sorted_list)

def triangle(r):
    for x in range(r):
        print(' '*(r-x-1) + "*"*(2*x+1))

triangle(9)
  