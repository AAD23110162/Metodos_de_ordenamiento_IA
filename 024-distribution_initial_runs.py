"""
024-distribution_initial_runs.py

Distribución de runs iniciales (simulación): dividir entrada en runs y asignar a ficheros/buckets.

Descripción: Detecta runs ascendentes en la entrada y asigna cada run a un bucket
de forma round-robin. Muestra cómo se generan los runs y cómo se asignan.

Autor: Alejandro Aguirre Díaz
"""
from typing import List
import sys


def distribute_runs(a: List[int], bucket_count: int, step: bool = False) -> List[List[List[int]]]:
    runs: List[List[int]] = []
    curr: List[int] = []
    for x in a:
        if not curr or x >= curr[-1]:
            curr.append(x)
        else:
            print(f"Run detectado: {curr}")
            runs.append(curr)
            curr = [x]
        if step:
            try:
                r = input("¿Continuar detección de runs? (s/n): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nInterrupción; terminando detección.")
                break
            if not r.startswith('s'):
                print("Detenido por el usuario durante la detección de runs.")
                break
    if curr:
        print(f"Run final detectado: {curr}")
        runs.append(curr)

    # asignar a buckets round-robin (simulado)
    buckets: List[List[List[int]]] = [[] for _ in range(bucket_count)]
    for i, r in enumerate(runs):
        idx = i % bucket_count
        print(f"Asignando run {r} al bucket {idx}")
        buckets[idx].append(r)
        if step:
            try:
                r = input("¿Continuar asignación a buckets? (s/n): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nInterrupción; terminando asignación.")
                break
            if not r.startswith('s'):
                print("Detenido por el usuario durante la asignación.")
                break
    return buckets


def main():
    demo = '--step' in [a.lower() for a in sys.argv[1:]]
    a = [1, 2, 6, 3, 4, 7, 5, 8, 9]
    print("Input:", a)
    buckets = distribute_runs(a, 3, step=demo)
    print("Buckets resultantes:")
    for i, b in enumerate(buckets):
        print(f"  bucket {i}: {b}")


if __name__ == '__main__':
    main()