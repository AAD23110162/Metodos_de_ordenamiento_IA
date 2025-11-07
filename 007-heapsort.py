"""
007-heapsort.py
HeapSort (método complejo según la guía).
"""
import sys

def heapify(a, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heapsort(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    return a

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [4,10,3,5,1]
        print("Demo input:", arr)
        print("Sorted:", heapsort(arr.copy()))
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted:", heapsort(arr))

if __name__ == "__main__":
    main()