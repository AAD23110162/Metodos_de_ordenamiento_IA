"""
022-balanced_multiway.py

Esquema simplificado de Balanced Multiway Merging: mezclar k runs a la vez.

Descripción: Mezcla k runs simultáneamente usando un heap (priority queue).
Muestra el heap inicial y cada extracción/inserción durante la mezcla.

Autor: Alejandro Aguirre Díaz
"""
from typing import List


def multiway_merge(runs: List[List[int]], step: bool = False) -> List[int]:
    import heapq
    heap: List[tuple] = []
    for i, run in enumerate(runs):
        if run:
            heap.append((run[0], i, 0))
    heapq.heapify(heap)
    print("Heap inicial:", heap)
    out: List[int] = []
    step_no = 0
    while heap:
        step_no += 1
        val, i, idx = heapq.heappop(heap)
        print(f"Paso {step_no}: pop {val} del run {i}, idx {idx}")
        out.append(val)
        if idx+1 < len(runs[i]):
            nxt = runs[i][idx+1]
            heapq.heappush(heap, (nxt, i, idx+1))
            print(f"  push {nxt} desde run {i}, nuevo heap: {heap}")
        else:
            print(f"  run {i} agotado")
        if step:
            try:
                resp = input("¿Continuar mezcla multiway? (s/n): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nInterrupción detectada; terminando.")
                break
            if not resp.startswith('s'):
                print("Detenido por el usuario.")
                break
    return out


def main():
    demo = '--step' in [a.lower() for a in __import__('sys').argv[1:]]
    runs = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print("Runs:", runs)
    merged = multiway_merge(runs, step=demo)
    print("Merged:", merged)