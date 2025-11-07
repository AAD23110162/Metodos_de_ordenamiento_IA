"""
013-hashing_sort.py
La guía incluye "Hashing" dentro de la familia de inserción.
Aquí se muestra un enfoque: distribuir en 'buckets' por función hash simple y ordenar cada bucket.
(No es un algoritmo de ordenación comparativa clásico.)
"""
import sys

def hashing_sort(a, buckets=10):
    if not a:
        return a
    minv, maxv = min(a), max(a)
    if minv == maxv:
        return a[:]
    size = (maxv - minv) / buckets + 1e-9
    bins = [[] for _ in range(buckets)]
    for x in a:
        idx = int((x - minv) / size)
        if idx >= buckets: idx = buckets-1
        bins[idx].append(x)
    res = []
    for b in bins:
        res.extend(sorted(b))
    return res

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [29,25,3,49,9,37,21,43]
        print("Demo input:", arr)
        print("Sorted (hashing/bucket):", hashing_sort(arr.copy()))
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted (hashing/bucket):", hashing_sort(arr))

if __name__ == "__main__":
    main()