"""
002-insertion_sort.py
Inserción directa (InsertionSort) mostrando pasos.

Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import List

def insertion_sort(a: List[int]) -> List[int]:
    print("Inicio Insertion Sort:", a)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        print(f"Insertando key={key} (pos {i})")
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
            print(f"  desplazando, estado: {a}")
        a[j+1] = key
        print(f"  colocado {key} en posición {j+1}, estado: {a}")
    print("Fin Insertion Sort:", a)
    return a

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == "demo"
    if demo:
        arr = [5, 2, 9, 1, 5, 6]
        print("Demo input:", arr)
        insertion_sort(arr)
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        insertion_sort(arr)

if __name__ == "__main__":
    main()