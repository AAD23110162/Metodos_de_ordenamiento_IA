"""
003-selection_sort.py

Selección directa (SelectionSort)
Descripción: Ordena una lista seleccionando repetidamente el mínimo;
muestra la selección e intercambios por iteración.

Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import List

def selection_sort(a: List[int]) -> List[int]:
    n = len(a)
    print("Inicio Selection Sort:", a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            print(f"Intercambiando a[{i}]={a[i]} con a[{min_idx}]={a[min_idx]}")
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"  estado después de iter {i}: {a}")
    print("Fin Selection Sort:", a)
    return a

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == "demo"
    if demo:
        arr = [64, 25, 12, 22, 11]
        print("Demo input:", arr)
        selection_sort(arr)
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        selection_sort(arr)

if __name__ == "__main__":
    main()