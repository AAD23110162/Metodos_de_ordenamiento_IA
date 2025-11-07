"""
010-tree_sort.py
Ordenamiento por árbol (Tree Sort) mostrando inserciones y recorrido inorder.
Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import Optional, List

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

def insert(root: Optional[Node], val: int) -> Node:
    if root is None:
        print(f"  creando nodo raíz {val}")
        return Node(val)
    if val <= root.val:
        print(f"  ir izq: insertar {val} en subárbol con raíz {root.val}")
        root.left = insert(root.left, val)
    else:
        print(f"  ir der: insertar {val} en subárbol con raíz {root.val}")
        root.right = insert(root.right, val)
    return root

def inorder(root: Optional[Node], out: List[int]) -> None:
    if root:
        inorder(root.left, out)
        out.append(root.val)
        print(f"  visitando nodo {root.val}")
        inorder(root.right, out)

def tree_sort(a: List[int]) -> List[int]:
    print("Inicio Tree Sort, entrada:", a)
    root: Optional[Node] = None
    for x in a:
        print(f"Insertando {x} en el BST")
        root = insert(root, x)
    out: List[int] = []
    print("Recorrido inorder:")
    inorder(root, out)
    print("Resultado ordenado:", out)
    return out

def main():
    demo = len(sys.argv) > 1 and sys.argv[1].lower() == 'demo'
    if demo:
        arr = [5, 3, 7, 2, 4, 6, 8]
        print("Demo input:", arr)
        tree_sort(arr)
    else:
        s = input("Ingrese números separados por espacios: ")
        arr = list(map(int, s.split())) if s.strip() else []
        tree_sort(arr)

if __name__ == '__main__':
    main()