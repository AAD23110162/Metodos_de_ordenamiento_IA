"""
011-radix_sort.py
RadixSort (para enteros no negativos).
"""
import sys

def counting_sort_for_radix(a, exp):
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

def radix_sort(a):
    if not a:
        return a
    max1 = max(a)
    exp = 1
    res = a[:]
    while max1 // exp > 0:
        res = counting_sort_for_radix(res, exp)
        exp *= 10
    return res

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [170,45,75,90,802,24,2,66]
        print("Demo input:", arr)
        print("Sorted:", radix_sort(arr.copy()))
    else:
        s = input("Ingrese enteros no negativos separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted:", radix_sort(arr))

if __name__ == "__main__":
    main()