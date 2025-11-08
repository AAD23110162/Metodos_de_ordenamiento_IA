Runner de demos de 020..024

Este directorio contiene utilidades para ejecutar los demos de los scripts externos
(020..024) que simulan algoritmos de ordenamiento externo.

Archivos:
- `run_demos_020_024.py`: ejecuta cada demo y guarda la salida en `outputs/`.
- `outputs/`: aquí se almacenan las salidas capturadas (creado por el runner).

Ejecutar (desde la raíz del repositorio):

```bash
python tests/run_demos_020_024.py
```

Para ver el comportamiento paso a paso con prompts, pasa `--step` (requiere
interacción manual):

```bash
python tests/run_demos_020_024.py --step
```

Nota: el runner no simula respuestas a los prompts interactivos; está pensado
para capturar las salidas no interactivas de los demos.
