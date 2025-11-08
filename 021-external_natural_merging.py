"""
021-external_natural_merging.py

Simulación de Natural Merging: detectar runs naturales en la entrada y mezclarlos.

Descripción: Detecta runs ascendentes ya existentes en la secuencia de entrada
y opcionalmente mezcla esos runs (usando la mezcla directa) mostrando los pasos.

Autor: Alejandro Aguirre Díaz
"""
from typing import List
import sys


def find_natural_runs(a: List[int]) -> List[List[int]]:
    runs: List[List[int]] = []
    if not a:
        return runs
    start = 0
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            runs.append(a[start:i])
            start = i
    runs.append(a[start:])
    return runs


def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == 'demo'
    step = '--step' in [a.lower() for a in sys.argv[1:]]
    if demo:
        a = [1, 2, 5, 3, 4, 8, 7, 9, 10]
        print("Input:", a)
        runs = find_natural_runs(a)
        print("Natural runs detectadas:", runs)
        # podemos usar la función de mezcla directa del módulo 020
        # Implementar una mezcla directa local para evitar problemas de import
        def straight_merge_local(runs_list, step_flag=False):
            runs_loc = [r[:] for r in runs_list]
            print("Mezclando runs detectadas (straight merging):")
            pass_no = 0
            while len(runs_loc) > 1:
                pass_no += 1
                print(f" Pass {pass_no}: mezclar pares -> {runs_loc}")
                new = []
                for i in range(0, len(runs_loc), 2):
                    if i+1 < len(runs_loc):
                        a, b = runs_loc[i], runs_loc[i+1]
                        merged = []
                        i1 = i2 = 0
                        while i1 < len(a) and i2 < len(b):
                            if a[i1] <= b[i2]:
                                merged.append(a[i1]); i1 += 1
                            else:
                                merged.append(b[i2]); i2 += 1
                        merged.extend(a[i1:]); merged.extend(b[i2:])
                        print(f"  merge {a} + {b} -> {merged}")
                        new.append(merged)
                    else:
                        print(f"  run sin pareja: {runs_loc[i]}")
                        new.append(runs_loc[i])
                runs_loc = new
                if step_flag:
                    try:
                        r = input("¿Desea continuar con la iteración? (s/n): ").strip().lower()
                    except (EOFError, KeyboardInterrupt):
                        print("\nInterrupción; terminando mezcla.")
                        break
                    if not r.startswith('s'):
                        print("Detenido por el usuario.")
                        break
            return runs_loc[0] if runs_loc else []

        result = straight_merge_local(runs, step_flag=step)
        print("Resultado final de la mezcla:", result)
    else:
        print("Ejemplo: ejecutar con 'python 021-external_natural_merging.py demo [--step]')")


if __name__ == '__main__':
    main()