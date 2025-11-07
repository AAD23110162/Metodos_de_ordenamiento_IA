"""
002-insertion_sort.py
Inserción directa (InsertionSort).
Modo:
  - demo: python 002-insertion_sort.py demo
  - interactivo: python 002-insertion_sort.py
"""
import sys

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [5,2,9,1,5,6]
        print("Demo input:", arr)
        print("Sorted:", insertion_sort(arr.copy()))
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted:", insertion_sort(arr))

if __name__ == "__main__":
    main()