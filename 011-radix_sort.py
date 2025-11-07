"""
011-radix_sort.py
RadixSort (para enteros no negativos) mostrando cada pasada por dígito.
Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import List

def counting_sort_for_radix(a: List[int], exp: int) -> List[int]:
    n = len(a)
    output = [0]*n
    count = [0]*10
    for i in range(n):
        index = (a[i] // exp) % 10
        count[index] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        index = (a[i] // exp) % 10
        output[count[index]-1] = a[i]
        count[index] -= 1
    return output

def radix_sort(a: List[int]) -> List[int]:
    if not a:
        return a
    max1 = max(a)
    exp = 1
    res = a[:]
    pass_no = 0
    while max1 // exp > 0:
        pass_no += 1
        print(f"Pass {pass_no}, exp={exp}, entrada: {res}")
        res = counting_sort_for_radix(res, exp)
        print(f"  salida después de pass {pass_no}: {res}")
        exp *= 10
    print("Resultado final:", res)
    return res

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == 'demo'
    if demo:
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        print("Demo input:", arr)
        radix_sort(arr)
    else:
        s = input("Ingrese enteros no negativos separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        radix_sort(arr)

if __name__ == '__main__':
    main()