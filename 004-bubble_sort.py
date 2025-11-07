"""
004-bubble_sort.py
Burbuja (BubbleSort) - familia de intercambio.
"""
import sys

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [3,2,1,4,5]
        print("Demo input:", arr)
        print("Sorted:", bubble_sort(arr.copy()))
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted:", bubble_sort(arr))

if __name__ == "__main__":
    main()