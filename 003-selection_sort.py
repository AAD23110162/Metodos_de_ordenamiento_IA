"""
003-selection_sort.py
Selección directa (SelectionSort).
"""
import sys

def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [64,25,12,22,11]
        print("Demo input:", arr)
        print("Sorted:", selection_sort(arr.copy()))
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted:", selection_sort(arr))

if __name__ == "__main__":
    main()