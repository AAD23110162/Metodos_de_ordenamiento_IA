"""
008-shellsort.py
ShellSort (algoritmo de inserción con gaps).
"""
import sys

def shell_sort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j-gap] > temp:
                a[j] = a[j-gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [12,34,54,2,3]
        print("Demo input:", arr)
        print("Sorted:", shell_sort(arr.copy()))
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted:", shell_sort(arr))

if __name__ == "__main__":
    main()