# CANON — Demo de tareas

## Producto
Función de dominio `agregar_tarea(tareas, titulo)` que devuelve una lista nueva con la tarea creada.

## Invariantes
- Título debe ser `str` y no quedar vacío después de `strip()`.
- La tarea añadida contiene `titulo` sin espacios extremos y `estado = "pendiente"`.
- La lista de entrada no debe mutarse.
- Se conservan elementos previos y su orden.

## Fuera de alcance
Persistencia, IDs, UI, autenticación, eliminación y ordenamiento.
