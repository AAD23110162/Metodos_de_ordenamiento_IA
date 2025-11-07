"""
021-external_natural_merging.py
Simulación de Natural Merging: detectar runs naturales en la entrada y mezclarlos.
"""
# Simplificado: detectar runs ascendentes
def find_natural_runs(a):
    runs = []
    if not a: return runs
    start = 0
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            runs.append(a[start:i])
            start = i
    runs.append(a[start:])
    return runs

def main():
    a = [1,2,5,3,4,8,7,9,10]
    print("Input:", a)
    runs = find_natural_runs(a)
    print("Natural runs:", runs)
    # Reusar straight_merge_simulation si desea mezclar (import simple)
    from .020_external_straight_merging import straight_merge_simulation if False else None
    # Nota: aquí se explica el proceso; implementación completa requeriría mezclar runs.
    print("Nota: se detectaron runs naturales; mezclar para orden final.")