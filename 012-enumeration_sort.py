"""
012-enumeration_sort.py
Clasificación por enumeración (determinística, O(n^2)).
Cada elemento cuenta cuántos elementos son menores para determinar su posición.
"""
import sys

def enumeration_sort(a):
    n = len(a)
    res = [None]*n
    for i in range(n):
        rank = 0
        for j in range(n):
            if a[j] < a[i] or (a[j] == a[i] and j < i):
                rank += 1
        res[rank] = a[i]
    return res

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [3,1,4,1,5,9]
        print("Demo input:", arr)
        print("Sorted:", enumeration_sort(arr.copy()))
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted:", enumeration_sort(arr))

if __name__ == "__main__":
    main()