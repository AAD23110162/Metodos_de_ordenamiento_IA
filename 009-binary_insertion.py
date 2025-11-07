"""
009-binary_insertion.py
Inserción binaria (optimiza búsqueda de posición).
"""
import sys
import bisect

def binary_insertion_sort(a):
    res = []
    for x in a:
        bisect.insort(res, x)
    return res

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [29,10,14,37,13]
        print("Demo input:", arr)
        print("Sorted:", binary_insertion_sort(arr.copy()))
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted:", binary_insertion_sort(arr))

if __name__ == "__main__":
    main()