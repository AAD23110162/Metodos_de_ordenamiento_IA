# Metodos_de_ordenamiento_IA
   
**Autor:** Alejandro Aguirre Díaz   
**Descripción:** Compilado de métodos de ordenamiento (implementaciones y plantillas de scripts).    
**Última modificación:** Jueves 6 de noviembre del 2025.

## Qué hay en este repositorio

Este repositorio contiene implementaciones y plantillas en Python de varios
métodos de ordenamiento mencionados en la guía de la UDB (Guía 3 — Programación IV).
Cada script sigue el formato "NNN-nombre.py" y puede ejecutarse en modo `demo`
o en modo interactivo (leer una lista de números desde la entrada estándar).

## Tipos de ordenamiento

- Internos: algoritmos que trabajan con los datos en memoria principal.
- Externos: algoritmos diseñados para ordenar datos que residen en memoria secundaria (archivos).

## Algoritmos incluidos (internos)
- `001-tree_sort.py` — Ordenamiento por árbol (Tree Sort).
- `002-insertion_sort.py` — Inserción directa (InsertionSort).
- `003-selection_sort.py` — Selección directa (SelectionSort).
- `004-bubble_sort.py` — Burbuja (familia de intercambio).
- `005-quicksort.py` — QuickSort (intercambio, rápido en promedio).
- `006-mergesort.py` — MergeSort (ordenamiento por mezcla, estable).
- `007-heapsort.py` — HeapSort (método complejo basado en montículos).
- `008-shellsort.py` — ShellSort (variación de inserción con gaps).
- `009-binary_insertion.py` — Inserción binaria (optimiza búsqueda de posición).
- `010-tree_sort.py` — Tree Sort (ordenamiento por árbol binario de búsqueda).
- `011-radix_sort.py` — RadixSort (ordenación por dígitos, para enteros).
- `012-enumeration_sort.py` — Clasificación por enumeración (posición mediante conteo).
- `013-hashing_sort.py` — Enfoque tipo "hash/bucket" (la guía menciona hashing en la familia de inserción).

## Algoritmos y utilidades externas (simulaciones / stubs)

- `020-external_straight_merging.py` — Simulación de mezclas directas (straight merging).
- `021-external_natural_merging.py` — Detección de runs naturales y explicación de mezcla.
- `022-balanced_multiway.py` — Multiway merge (mezcla balanceada con heap).
- `023-polyphase.py` — Esqueleto/explicación de Polyphase Sort (requiere I/O real para una implementación completa).
- `024-distribution_initial_runs.py` — Distribución de runs iniciales (simulación de buckets/files).

## Clasificación por familias (según la guía)

- Inserción: Inserción directa, ShellSort, Inserción binaria, Hashing (bucket).
- Intercambio: Burbuja, QuickSort.
- Selección: Selección directa.
- Enumeración: Enumeration sort (descrito y provisto).

## Cómo ejecutar un script (ejemplo)

Ejecutar el demo de `insertion_sort`:

```bash
python 002-insertion_sort.py demo
```

Ejecutar en modo interactivo (leer números desde stdin):

```bash
python 002-insertion_sort.py
# luego escribir: 5 2 9 1 3
```

## Notas

- Para los algoritmos externos he incluido simulaciones y stubs porque una
	implementación completa requiere manejo de archivos, lectura/escritura en disco y
	generación de runs (más adecuada para datasets grandes y pruebas externas).
- La guía que motivó estas plantillas incluye ejemplos en C# de Burbuja e
	InsertionSort; aquí se han proporcionado equivalentes en Python como referencia.

## Siguientes pasos sugeridos

- Completar la descarga y extracción del PDF para incorporar citas y páginas exactas (tarea pendiente en el TODO).
- Añadir pruebas unitarias para cada script.
- Implementar versiones con I/O sobre archivos para los métodos externos si se desea probar con datasets grandes.


