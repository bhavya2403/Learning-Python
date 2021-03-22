#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

count = 0
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            (a[j], a[j+1]) = (a[j+1], a[j])
            count += 1
            swapped = True
                
    if not swapped:
        break

print("Array is sorted in " + str(count) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n-1]))
