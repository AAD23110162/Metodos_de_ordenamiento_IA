"""
010-tree_sort.py
Ordenamiento por árbol (Tree Sort) usando BST simple.
"""
import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val <= root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root, out):
    if root:
        inorder(root.left, out)
        out.append(root.val)
        inorder(root.right, out)

def tree_sort(a):
    root = None
    for x in a:
        root = insert(root, x)
    out = []
    inorder(root, out)
    return out

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [5,3,7,2,4,6,8]
        print("Demo input:", arr)
        print("Sorted:", tree_sort(arr.copy()))
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split()))
        print("Sorted:", tree_sort(arr))

if __name__ == "__main__":
    main()