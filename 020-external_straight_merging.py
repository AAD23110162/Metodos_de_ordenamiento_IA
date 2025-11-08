"""
020-external_straight_merging.py

Simulación simple de Straight Merging (mezclas directas) usando listas como 'fueses' de disco.
En un entorno real se usan archivos y ficheros temporales.

Descripción: Toma una lista de "runs" ordenadas y las mezcla en pares
sucesivamente (pasadas) hasta obtener una única secuencia ordenada. Muestra
cada paso de mezcla y el estado intermedio.

Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import List


def straight_merge_simulation(runs: List[List[int]], step: bool = False) -> List[int]:
    """Mezcla las runs en pares hasta obtener una sola run.

    Si step=True, imprime y pregunta tras cada mezcla si continuar.
    """
    runs_local = [r[:] for r in runs]
    pass_no = 0
    print("Estado inicial de runs:", runs_local)
    while len(runs_local) > 1:
        pass_no += 1
        print(f"\nPass {pass_no}: mezclar runs en pares (total runs={len(runs_local)})")
        new_runs: List[List[int]] = []
        for i in range(0, len(runs_local), 2):
            if i + 1 < len(runs_local):
                a, b = runs_local[i], runs_local[i+1]
                print(f"  Mezclando run {i}: {a}  con run {i+1}: {b}")
                merged: List[int] = []
                i1 = i2 = 0
                while i1 < len(a) and i2 < len(b):
                    if a[i1] <= b[i2]:
                        merged.append(a[i1]); i1 += 1
                    else:
                        merged.append(b[i2]); i2 += 1
                if i1 < len(a):
                    merged.extend(a[i1:])
                if i2 < len(b):
                    merged.extend(b[i2:])
                print(f"    resultado merge: {merged}")
                new_runs.append(merged)
            else:
                print(f"  run sin pareja, se lleva adelante: {runs_local[i]}")
                new_runs.append(runs_local[i])
        runs_local = new_runs
        print(f"  estado runs tras pass {pass_no}: {runs_local}")
        if step:
            try:
                resp = input("¿Desea continuar con la iteración? (s/n): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nInterrupción detectada; terminando.")
                break
            if not resp.startswith('s'):
                print("Detenido por el usuario.")
                break
    return runs_local[0] if runs_local else []


def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == 'demo'
    step = '--step' in [a.lower() for a in sys.argv[1:]]
    if demo:
        runs = [[1, 3, 5], [2, 4, 6], [7, 9], [8, 10]]
        print("Runs de ejemplo:", runs)
        result = straight_merge_simulation(runs, step=step)
        print("\nResultado final:", result)
    else:
        print("Ejemplo: ejecutar con 'python 020-external_straight_merging.py demo [--step]')")