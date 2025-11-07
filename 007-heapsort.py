"""
007-heapsort.py

Descripción: Implementa HeapSort; muestra la construcción del 
heap (heapify) y las extracciones sucesivas de la raíz.

Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import List

def heapify(a: List[int], n: int, i: int, depth=0) -> None:
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        print(f"heapify: swap a[{i}]={a[i]} <-> a[{largest}]={a[largest]} (n={n})")
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest, depth+1)

def heapsort(a: List[int]) -> List[int]:
    n = len(a)
    print("Inicio HeapSort, lista:", a)
    # build heap
    for i in range(n//2 - 1, -1, -1):
        print(f"Construyendo heap desde i={i}")
        heapify(a, n, i)
        print(f"  heap parcial: {a}")
    # extract
    for i in range(n-1, 0, -1):
        print(f"Swap raiz {a[0]} con a[{i}]={a[i]}")
        a[0], a[i] = a[i], a[0]
        print(f"  después swap: {a}")
        heapify(a, i, 0)
        print(f"  heapify con n={i}: {a}")
    print("Fin HeapSort:", a)
    return a

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == 'demo'
    if demo:
        arr = [4, 10, 3, 5, 1]
        print("Demo input:", arr)
        heapsort(arr)
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        heapsort(arr)

if __name__ == '__main__':
    main()