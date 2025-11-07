"""
012-enumeration_sort.py

Descripción: Implementa Enumeration Sort; para cada 
elemento calcula su posición (rank) en la lista y construye el resultado, 
mostrando los cálculos paso a paso.

Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import List

def enumeration_sort(a: List[int]) -> List[int]:
    n = len(a)
    res: List[int] = [None] * n
    print("Inicio Enumeration Sort, entrada:", a)
    for i in range(n):
        rank = 0
        for j in range(n):
            if a[j] < a[i] or (a[j] == a[i] and j < i):
                rank += 1
        print(f"  elemento a[{i}]={a[i]} -> rank={rank}")
        res[rank] = a[i]
        print(f"   res parcial: {res}")
    print("Resultado final:", res)
    return res

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == 'demo'
    if demo:
        arr = [3, 1, 4, 1, 5, 9]
        print("Demo input:", arr)
        enumeration_sort(arr)
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        enumeration_sort(arr)

if __name__ == '__main__':
    main()