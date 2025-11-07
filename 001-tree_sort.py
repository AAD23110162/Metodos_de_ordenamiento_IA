"""
001-tree_sort.py

Ordenamiento por árbol (Tree Sort) — implementación educativa con trazas.

Entrada: números enteros separados por espacios.
Salida: lista ordenada en stdout.

Tree Sort construye un BST y realiza un recorrido inorder para obtener
la secuencia ordenada.

Autor: Alejandro Aguirre Díaz
"""
import sys
from typing import Optional, List


class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None


def ask_continue() -> bool:
    """Pregunta al usuario si desea continuar la iteración.

    Retorna True para continuar, False para detener.
    """
    try:
        resp = input("¿Desea continuar con la iteración? (s/n): ").strip().lower()
    except EOFError:
        # si no hay más entrada, continuar por defecto
        return True
    except KeyboardInterrupt:
        # si el usuario interrumpe con Ctrl+C, tratamos como "no" (detener)
        print("\nInterrumpido por el usuario durante la confirmación.")
        return False
    return resp.startswith('s')


def insert(root: Optional[Node], val: int, step: bool = False) -> Node:
    """Inserta val en el BST (permite duplicados, colocándolos a la izquierda).

    Si step=True, pregunta al usuario después de la inserción si desea continuar.
    """
    if root is None:
        print(f"  creando nodo {val}")
        node = Node(val)
        if step and not ask_continue():
            print("Iteración detenida por el usuario.")
            sys.exit(0)
        return node
    if val <= root.val:
        print(f"  insertar {val} en subárbol izquierdo de {root.val}")
        root.left = insert(root.left, val, step)
    else:
        print(f"  insertar {val} en subárbol derecho de {root.val}")
        root.right = insert(root.right, val, step)
    if step and not ask_continue():
        print("Iteración detenida por el usuario.")
        sys.exit(0)
    return root


def inorder(root: Optional[Node], out: List[int], step: bool = False) -> None:
    if root is None:
        return
    inorder(root.left, out, step)
    out.append(root.val)
    print(f"  visitando {root.val}")
    if step and not ask_continue():
        print("Iteración detenida por el usuario.")
        sys.exit(0)
    inorder(root.right, out, step)


def tree_sort(arr: List[int], step: bool = False) -> List[int]:
    print("Inicio Tree Sort, entrada:", arr)
    root: Optional[Node] = None
    for x in arr:
        print(f"Insertando {x}...")
        root = insert(root, x, step)
    out: List[int] = []
    print("Recorrido inorder:")
    inorder(root, out, step)
    print("Resultado ordenado:", out)
    return out


def parse_input(s: str) -> List[int]:
    if not s.strip():
        return []
    parts = s.strip().split()
    return [int(p) for p in parts]


def main():
    step = False
    args = [a.lower() for a in sys.argv[1:]]
    demo = 'demo' in args
    if '--step' in args or '-s' in args or 'step' in args:
        step = True

    if demo:
        arr = [5, 3, 7, 2, 4, 6, 8]
        print("Demo input:", arr)
        tree_sort(arr.copy(), step=step)
        return

    try:
        s = input("Ingrese números enteros separados por espacios: ")
    except EOFError:
        print("No se recibió entrada.", file=sys.stderr)
        return
    except KeyboardInterrupt:
        # Manejar Ctrl+C de forma limpia
        print("\nEjecución interrumpida por el usuario.")
        return
    try:
        arr = parse_input(s)
    except ValueError:
        print("Entrada inválida: todos los tokens deben ser enteros", file=sys.stderr)
        return
    tree_sort(arr, step=step)


if __name__ == "__main__":
    main()