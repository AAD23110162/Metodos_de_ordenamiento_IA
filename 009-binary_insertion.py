"""
009-binary_insertion.py

Inserción binaria
Descripción: Implementa inserción binaria 
usando bisect.insort; muestra la lista resultante tras cada inserción.

Autor: Alejandro Aguirre Díaz
"""
import sys
import bisect
from typing import List

def binary_insertion_sort(a: List[int]) -> List[int]:
    res: List[int] = []
    print("Inicio Binary Insertion Sort, entrada:", a)
    for x in a:
        bisect.insort(res, x)
        print(f"  inserta {x} -> {res}")
    print("Fin Binary Insertion Sort:", res)
    return res

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == 'demo'
    if demo:
        arr = [29, 10, 14, 37, 13]
        print("Demo input:", arr)
        binary_insertion_sort(arr)
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        binary_insertion_sort(arr)

if __name__ == '__main__':
    main()