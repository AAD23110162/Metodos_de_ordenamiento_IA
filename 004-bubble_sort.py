"""
004-bubble_sort.py
Burbuja (BubbleSort) mostrando pasos.
Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import List

def bubble_sort(a: List[int]) -> List[int]:
    n = len(a)
    print("Inicio Bubble Sort:", a)
    for i in range(n):
        swapped = False
        print(f"Pass {i+1}:")
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                print(f"  swap a[{j}]={a[j]} <-> a[{j+1}]={a[j+1]}")
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
                print(f"   estado: {a}")
        if not swapped:
            print("  No hubo swaps, lista ordenada")
            break
    print("Fin Bubble Sort:", a)
    return a

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == "demo"
    if demo:
        arr = [3, 2, 1, 4, 5]
        print("Demo input:", arr)
        bubble_sort(arr)
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        bubble_sort(arr)

if __name__ == "__main__":
    main()