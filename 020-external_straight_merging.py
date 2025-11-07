"""
020-external_straight_merging.py
Simulación simple de Straight Merging (mezclas directas) usando listas como 'fueses' de disco.
En un entorno real se usan archivos y ficheros temporales.
Autor: Alejandro Aguirre Díaz
"""
import sys
from collections import deque
import math

def straight_merge_simulation(runs):
    # runs: lista de listas (runs ya ordenadas)
    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), 2):
            if i+1 < len(runs):
                a, b = runs[i], runs[i+1]
                merged = []
                i1 = i2 = 0
                while i1 < len(a) and i2 < len(b):
                    if a[i1] <= b[i2]:
                        merged.append(a[i1]); i1 += 1
                    else:
                        merged.append(b[i2]); i2 += 1
                merged.extend(a[i1:]); merged.extend(b[i2:])
                new_runs.append(merged)
            else:
                new_runs.append(runs[i])
        runs = new_runs
    return runs[0] if runs else []

def main():
    print("Ejemplo de mezcla directa (runs simuladas).")
    runs = [[1,3,5],[2,4,6],[7,9],[8,10]]
    print("Runs:", runs)
    print("Resultado:", straight_merge_simulation(runs))