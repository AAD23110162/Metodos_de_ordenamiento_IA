# Metodos de ordenamiento IA
   
**Autor:** Alejandro Aguirre Díaz   
**Descripción:** Compilado de métodos de ordenamiento (implementaciones y plantillas de scripts).    
**Última modificación:** Jueves 6 de noviembre del 2025.

## Tipos de ordenamiento

- Internos: algoritmos que trabajan con los datos en memoria principal.
- Externos: algoritmos diseñados para ordenar datos que residen en memoria secundaria (archivos).

## Algoritmos internos
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

## Detalles de los algoritmos

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

## Clasificación por familias

- Inserción: Inserción directa, ShellSort, Inserción binaria, Hashing (bucket).
- Intercambio: Burbuja, QuickSort.
- Selección: Selección directa.
- Enumeración: Enumeration sort (descrito y provisto).

## Glosario técnico

Este glosario ofrece definiciones breves de términos y conceptos usados a lo largo del repositorio. Está pensado para que el lector comprenda rápidamente la terminología empleada en los scripts y descripciones.

- Algoritmo: conjunto finito de instrucciones que transforma una entrada en una salida. En este repositorio, se refiere a rutinas de ordenamiento.
- Estabilidad (stable): propiedad de un algoritmo de ordenamiento que preserva el orden relativo de elementos iguales.
- In-place: algoritmo que realiza la ordenación usando espacio adicional constante O(1) (no requiere una copia completa de los datos).
- Out-of-place / extra espacio: algoritmos que necesitan espacio adicional proporcional a la entrada (p. ej. O(n)).
- Complejidad temporal (Big O): medida asintótica del tiempo de ejecución en función del tamaño de entrada n; se suele indicar por peor, promedio y mejor caso (O(n), O(n log n), O(n^2), etc.).
- Complejidad espacial: cantidad de memoria adicional requerida por el algoritmo además de la entrada.
- Caso mejor/promedio/peor: escenarios de entrada que provocan el mejor, el comportamiento típico y el peor rendimiento del algoritmo.
- Run (corrida/serie ordenada): subsecuencia contigua de la entrada que ya está ordenada ascendentemente; concepto clave en ordenación externa (natural runs).
- Mezcla / merge: operación que combina dos (o más) runs ordenadas en una única secuencia ordenada.
- Paso/pasada (pass): una iteración completa sobre el conjunto de datos o sobre una estructura de runs (usado en mezclas externas).
- Heap (montículo): estructura de datos tipo árbol que permite extraer el máximo o mínimo eficientemente; usada en HeapSort y k-way merges.
- BST (árbol binario de búsqueda): estructura de árbol donde para cada nodo, los valores menores están a la izquierda y los mayores a la derecha; se usa en Tree Sort e inorder traversal.
- Inorder traversal (recorrido inorder): visita de un BST que produce los elementos en orden ascendente.
- Pivot (pivote): elemento elegido en QuickSort para particionar la lista en menores y mayores.
- Partición (partition): proceso de reorganizar la lista según el pivote durante QuickSort.
- k-way merge (mezcla k-vías): combinación de k runs ordenadas a la vez, normalmente implementada con una cola de prioridad (heap) para eficiencia.
- Polyphase: estrategia de ordenación externa que distribuye runs entre ficheros según patrones (p. ej. Fibonacci) para equilibrar pasadas y minimizar I/O; aquí se presenta como esqueleto didáctico.
- Bucket / Bins (cubetas): contenedores en los que se distribuyen elementos por una función de mapeo antes de ordenar cada cubeta (Bucket Sort / hashing-like).
- Counting sort: ordenamiento estable por conteo que cuenta ocurrencias de claves (útil como subrutina en Radix Sort).
- Radix sort: ordenamiento por dígitos que aplica un ordenamiento estable por cada posición de dígito (LSD o MSD).
- Adaptativo / presortedness: grado en que una entrada ya está ordenada; algoritmos adaptativos aprovechan presortedness para mejorar el rendimiento.
- Recursión / profundidad de recursión: llamada repetida a una función desde sí misma; importante para QuickSort y MergeSort (control de pila/stack).
- I/O passes (pasadas de E/S): en ordenación externa, cantidad de lecturas/escrituras secuenciales sobre ficheros necesarias para obtener el resultado final.
- Buffer: área de memoria temporal usada para acumular datos leídos/escritos antes de realizar operaciones de E/S; reducir pases y optimizar buffers mejora el rendimiento externo.
- Distribución round-robin: forma simple de asignar runs a múltiples ficheros/cubetas de manera cíclica.
- Estimación amortizada: análisis que promedia el coste de una operación a lo largo de una secuencia de operaciones para obtener un coste medio por operación.




