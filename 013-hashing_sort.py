"""
013-hashing_sort.py
Hashing / bucket sort (enfoque educativo) mostrando distribución y buckets.
Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import List

def hashing_sort(a: List[int], buckets: int = 10) -> List[int]:
    print("Inicio Hashing/Bucket Sort, entrada:", a)
    if not a:
        return a
    minv, maxv = min(a), max(a)
    if minv == maxv:
        print("Todos los elementos iguales.")
        return a[:]
    size = (maxv - minv) / buckets + 1e-9
    bins: List[List[int]] = [[] for _ in range(buckets)]
    for x in a:
        idx = int((x - minv) / size)
        if idx >= buckets:
            idx = buckets - 1
        bins[idx].append(x)
        print(f"  {x} -> bucket {idx}")
    for i, b in enumerate(bins):
        print(f"Bucket {i}: {b}")
    res: List[int] = []
    for i, b in enumerate(bins):
        if b:
            b_sorted = sorted(b)
            print(f"  ordenar bucket {i}: {b} -> {b_sorted}")
            res.extend(b_sorted)
    print("Resultado final:", res)
    return res

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == 'demo'
    if demo:
        arr = [29,25,3,49,9,37,21,43]
        print("Demo input:", arr)
        hashing_sort(arr)
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        hashing_sort(arr)

if __name__ == '__main__':
    main()