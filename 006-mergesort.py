"""
006-mergesort.py
MergeSort (ordenamiento por mezcla) mostrando splits/merges.
Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import List

def mergesort(a: List[int], depth=0) -> List[int]:
    prefix = '  ' * depth
    if len(a) <= 1:
        print(f"{prefix}Base case: {a}")
        return a
    mid = len(a)//2
    print(f"{prefix}Split: {a} -> left={a[:mid]}, right={a[mid:]}")
    left = mergesort(a[:mid], depth+1)
    right = mergesort(a[mid:], depth+1)
    merged = merge(left, right)
    print(f"{prefix}Merged {left} + {right} -> {merged}")
    return merged

def merge(l: List[int], r: List[int]) -> List[int]:
    res: List[int] = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i]); i += 1
        else:
            res.append(r[j]); j += 1
    res.extend(l[i:]); res.extend(r[j:])
    return res

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == 'demo'
    if demo:
        arr = [38, 27, 43, 3, 9, 82, 10]
        print("Demo input:", arr)
        mergesort(arr)
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        print("Sorted:", mergesort(arr))

if __name__ == '__main__':
    main()