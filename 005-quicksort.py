"""
005-quicksort.py
QuickSort (familia de intercambio).
Implementación in-place (hoare/lamuto simplificado).
"""
import sys
sys.setrecursionlimit(10000)

def quicksort(a, lo=0, hi=None):
    if hi is None:
        hi = len(a)-1
    if lo < hi:
        p = partition(a, lo, hi)
        quicksort(a, lo, p-1)
        quicksort(a, p+1, hi)
    return a

def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [10,7,8,9,1,5]
        print("Demo input:", arr)
        print("Sorted:", quicksort(arr.copy()))
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted:", quicksort(arr))

if __name__ == "__main__":
    main()