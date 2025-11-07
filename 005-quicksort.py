"""
005-quicksort.py
QuickSort (familia de intercambio) mostrando pasos (particiones y swaps).
Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import List
sys.setrecursionlimit(10000)

def quicksort(a: List[int], lo=0, hi=None) -> List[int]:
    if hi is None:
        hi = len(a)-1
    if lo < hi:
        p = partition(a, lo, hi)
        print(f"Después partición pivot_index={p}, estado: {a}")
        quicksort(a, lo, p-1)
        quicksort(a, p+1, hi)
    return a

def partition(a: List[int], lo: int, hi: int) -> int:
    pivot = a[hi]
    print(f"Partition llamado en a[{lo}:{hi+1}]={a[lo:hi+1]}, pivot={pivot}")
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            print(f"  swap a[{i}]={a[i]} <-> a[{j}]={a[j]}")
            a[i], a[j] = a[j], a[i]
            i += 1
    print(f"  colocando pivot a[{i}] (valor {a[hi]})")
    a[i], a[hi] = a[hi], a[i]
    return i

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == "demo"
    if demo:
        arr = [10, 7, 8, 9, 1, 5]
        print("Demo input:", arr)
        quicksort(arr)
        print("Sorted:", arr)
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        quicksort(arr)
        print("Sorted:", arr)

if __name__ == "__main__":
    main()