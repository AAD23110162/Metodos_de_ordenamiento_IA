"""
006-mergesort.py
MergeSort (ordenamiento por mezcla).
"""
import sys

def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    return merge(left, right)

def merge(l, r):
    res = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i]); i += 1
        else:
            res.append(r[j]); j += 1
    res.extend(l[i:]); res.extend(r[j:])
    return res

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [38,27,43,3,9,82,10]
        print("Demo input:", arr)
        print("Sorted:", mergesort(arr.copy()))
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted:", mergesort(arr))

if __name__ == "__main__":
    main()