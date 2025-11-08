# Metodos_de_ordenamiento_IA
   
**Autor:** Alejandro Aguirre Díaz   
**Descripción:** Compilado de métodos de ordenamiento (implementaciones y plantillas de scripts).    
**Última modificación:** Jueves 6 de noviembre del 2025.

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

## Detalles de los algoritmos (descripciones breves y características)

A continuación se encuentran descripciones más detalladas de cada algoritmo incluido, con una nota sobre su complejidad, estabilidad y uso típico.

- `001-tree_sort.py` — Tree Sort
	- Idea: inserta los elementos en un árbol binario de búsqueda (BST) y realiza un recorrido inorder para obtener la lista ordenada.
	- Complejidad: promedio O(n log n), peor caso O(n^2) si el árbol queda degenerado (entrada ya ordenada).
	- Espacio: O(n) adicional para el árbol.
	- Estable: no necesariamente (depende de la convención para duplicados).
	- Uso: didáctico; muestra la relación entre estructuras de datos y ordenación.

- `002-insertion_sort.py` — Insertion Sort
	- Idea: construye la porción ordenada a la izquierda insertando cada elemento en su posición correcta.
	- Complejidad: O(n^2) promedio/peor, O(n) mejor cuando la lista ya está casi ordenada.
	- Espacio: O(1) (in-place).
	- Estable: sí.
	- Uso: muy eficiente para listas pequeñas o casi ordenadas; útil en híbridos (p. ej. introsort, timsort).

- `003-selection_sort.py` — Selection Sort
	- Idea: en cada iteración selecciona el elemento mínimo del resto y lo coloca en su posición final.
	- Complejidad: O(n^2) en todos los casos.
	- Espacio: O(1) (in-place), número de swaps es mínimo (O(n)).
	- Estable: no por defecto (se puede adaptar).
	- Uso: simple, útil para enseñanza; rara vez usado en producción por su complejidad.

- `004-bubble_sort.py` — Bubble Sort
	- Idea: repetidamente recorre la lista y realiza intercambios adyacentes para 'flotar' elementos grandes hacia el final.
	- Complejidad: O(n^2) promedio/peor, O(n) mejor si se detecta sin swaps.
	- Espacio: O(1) (in-place).
	- Estable: sí.
	- Uso: educativo; su optimización con flag lo hace detectar rápidamente listas ya ordenadas.

- `005-quicksort.py` — QuickSort
	- Idea: dividir y conquistar: elegir un pivote, particionar la lista y ordenar recursivamente las sublistas.
	- Complejidad: O(n log n) promedio, O(n^2) peor (pivote malo o entrada degenerada).
	- Espacio: in-place (recursión usa O(log n) en promedio para la pila).
	- Estable: no (por defecto).
	- Uso: algoritmo de propósito general muy rápido en la práctica; elegir buen pivote y/o aleatorizar para evitar peor caso.

- `006-mergesort.py` — MergeSort
	- Idea: divide la lista en mitades, ordena recursivamente y mezcla las mitades ordenadas.
	- Complejidad: O(n log n) en todos los casos.
	- Espacio: requiere O(n) adicional en la implementación típica (no in-place).
	- Estable: sí.
	- Uso: excelente para estructuras enlazadas y para ordenación externa (merge es naturalmente secuencial).

- `007-heapsort.py` — HeapSort
	- Idea: construir un heap máximo y extraer repetidamente la raíz para construir la lista ordenada.
	- Complejidad: O(n log n) en todos los casos.
	- Espacio: O(1) adicional (in-place).
	- Estable: no.
	- Uso: cuando se necesita una garantía de peor caso O(n log n) y operación in-place.

- `008-shellsort.py` — ShellSort
	- Idea: mejora la inserción usando 'gaps' (secuencias de separación) para mover elementos más rápido hacia su posición.
	- Complejidad: depende de la secuencia de gaps; típicamente entre O(n log^2 n) y O(n^2).
	- Espacio: O(1) (in-place).
	- Estable: no.
	- Uso: práctico en arreglos pequeños/medianos; comportamiento y rendimiento dependen fuertemente de la secuencia de gaps.

- `009-binary_insertion.py` — Binary Insertion Sort
	- Idea: utiliza búsqueda binaria para encontrar la posición de inserción pero aún desplaza elementos (movimientos O(n)).
	- Complejidad: O(n^2) tiempo (mejora en comparaciones), O(1) espacio.
	- Estable: sí.
	- Uso: reduce comparaciones frente a insertion sort, útil cuando las comparaciones son costosas.

- `010-tree_sort.py` — Tree Sort (versión adicional)
	- Nota: este repositorio incluye dos plantillas de Tree Sort (`001` y `010`), ambas con trazas; ver `001-tree_sort.py` para la versión con paso a paso interactivo.

- `011-radix_sort.py` — Radix Sort
	- Idea: ordena por dígitos desde el menos significativo al más significativo (o viceversa), usando un ordenamiento estable por dígito (p. ej. counting sort).
	- Complejidad: O(n * k) donde k es el número de dígitos; eficiente para enteros con rango limitado.
	- Espacio: O(n + b) (b = base/dígitos), estable si el subordenamiento por dígito es estable.
	- Uso: ordenar enteros grandes de forma lineal respecto a n (cuando k es pequeño/constante).

- `012-enumeration_sort.py` — Enumeration Sort
	- Idea: para cada elemento cuenta cuántos elementos son menores (o iguales con criterio) para deducir su posición final.
	- Complejidad: O(n^2).
	- Espacio: O(n) para la salida.
	- Estable: puede ser diseñada estable con reglas de desempate.
	- Uso: puramente educativo; útil para entender conceptos de ranking y posicionamiento.

- `013-hashing_sort.py` — Hashing / Bucket Sort
	- Idea: distribuir elementos en buckets según una función de hashing (o función de mapeo) y ordenar cada bucket por separado.
	- Complejidad: promedio O(n + k) (k = número de buckets), depende de la distribución.
	- Espacio: O(n + k).
	- Estable: depende de cómo se ordenen internamente los buckets (si se usa un ordenamiento estable, sí).
	- Uso: muy eficiente cuando la entrada se distribuye uniformemente entre buckets (ej. bucket sort para floats en [0,1)).

## Descripción de utilidades externas (020..024)

- `020-external_straight_merging.py` — Straight merging (mezcla directa)
	- Idea: mezcla runs ordenadas en pares a lo largo de múltiples pasadas hasta obtener una sola secuencia ordenada; simulación local usando listas.
	- Uso: técnica central en algoritmos de ordenamiento externo (cuando los datos no caben en memoria).

- `021-external_natural_merging.py` — Natural merging
	- Idea: detecta runs ya existentes (runs naturales) en la entrada y las mezcla; a menudo reduce el número de pasadas necesarias.

- `022-balanced_multiway.py` — Balanced multiway merging
	- Idea: mezcla k runs a la vez usando un heap (priority queue), reduciendo el número de pasadas requeridas en comparación con mezclas binarias.
	- Uso: muy útil en ordenamiento externo cuando se tienen k ficheros/dispositivos de entrada.

- `023-polyphase.py` — Polyphase Sort (esqueleto)
	- Idea: estrategia avanzada para ordenar externamente que distribuye runs entre ficheros según series de Fibonacci para equilibrar el trabajo y minimizar accesos.
	- Nota: esta implementación es un stub explicativo (sin I/O de ficheros) para fines didácticos.

- `024-distribution_initial_runs.py` — Distribución de runs iniciales
	- Idea: detecta runs ascendentes en la entrada y los asigna a buckets/ficheros (p. ej. round-robin) como paso preliminar antes de las mezclas externas.


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


