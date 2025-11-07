"""
001-tree_sort.py
--------------------------------
Ordenamiento por árbol (Tree Sort) — implementación educativa.

Modos:
  - demo: python 001-tree_sort.py demo
  - interactivo: python 001-tree_sort.py  (leer números por stdin)

Entrada: números enteros separados por espacios.
Salida: lista ordenada en stdout.

Nota: Tree Sort construye un BST y realiza un recorrido inorder para obtener
la secuencia ordenada. En árboles sin balancear, el peor caso es O(n^2).
Autor: <tu nombre>
"""
import sys
from typing import Optional, List

class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

def insert(root: Optional[Node], val: int) -> Node:
    """Inserta val en el BST (permite duplicados, colocándolos a la izquierda o derecha según convención)."""
    if root is None:
        return Node(val)
    if val <= root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root: Optional[Node], out: List[int]) -> None:
    """Recorrido inorder que recolecta valores en orden ascendente."""
    if root is None:
        return
    inorder(root.left, out)
    out.append(root.val)
    inorder(root.right, out)

def tree_sort(arr: List[int]) -> List[int]:
    """Ordena arr usando BST + inorder."""
    root: Optional[Node] = None
    for x in arr:
        root = insert(root, x)
    result: List[int] = []
    inorder(root, result)
    return result

def parse_input(s: str) -> List[int]:
    """Convierte una cadena de entrada en lista de enteros; lanza ValueError si hay tokens inválidos."""
    if not s.strip():
        return []
    parts = s.strip().split()
    try:
        return [int(p) for p in parts]
    except ValueError as e:
        raise ValueError("Entrada inválida: todos los tokens deben ser enteros") from e

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        arr = [5, 3, 7, 2, 4, 6, 8]  # demo
        print("Demo input:", arr)
        print("Sorted:", tree_sort(arr.copy()))
        return

    # modo interactivo
    try:
        s = input("Ingrese números enteros separados por espacios: ")
    except EOFError:
        print("No se recibió entrada.", file=sys.stderr)
        return

    try:
        arr = parse_input(s)
    except ValueError as err:
        print(err, file=sys.stderr)
        return

    print("Sorted:", tree_sort(arr))

if __name__ == "__main__":
    main()