"""
008-shellsort.py
ShellSort (algoritmo de inserción con gaps) mostrando pasos.
Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import List

def shell_sort(a: List[int]) -> List[int]:
    n = len(a)
    gap = n // 2
    print("Inicio ShellSort:", a)
    while gap > 0:
        print(f"Gap = {gap}")
        for i in range(gap, n):
            temp = a[i]
            j = i
            print(f"  Insertando {temp} en sublista con gap, inicio j={j}")
            while j >= gap and a[j-gap] > temp:
                a[j] = a[j-gap]
                j -= gap
                print(f"   desplazando, estado: {a}")
            a[j] = temp
            print(f"   colocado {temp} en pos {j}, estado: {a}")
        gap //= 2
    print("Fin ShellSort:", a)
    return a

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == 'demo'
    if demo:
        arr = [12, 34, 54, 2, 3]
        print("Demo input:", arr)
        shell_sort(arr)
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        shell_sort(arr)

if __name__ == '__main__':
    main()