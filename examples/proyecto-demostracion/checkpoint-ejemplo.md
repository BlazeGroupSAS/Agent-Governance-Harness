# CP-001 — Agregar tarea

**Frente:** demo-alta-tareas.

**Base Git:** establecer SHA real al comenzar una implementación. Este documento es un ejemplo y no registra una ejecución remota.

**Objetivo:** agregar una tarea validada y devolver una nueva lista.

**Archivos permitidos:** `tareas.py`, `test_tareas.py`, `STATE.md`.

**Exclusiones:** base de datos, API, interfaz y despliegue.

**Pruebas:** `python -m unittest -v`. Registrar resultado y código de salida observado.

**Aceptación:** rechaza textos vacíos y tipos inválidos; mantiene el orden y la lista original; tarea nueva en estado pendiente.

**Auditoría:** revisar cumplimiento de CANON y diff de la referencia real; si se rechaza, remediar y presentar un nuevo SHA.

**Reversión:** descartar la rama aislada si no hay integración; usar revert del commit si ya se integró.

**Permisos:** este ejemplo no autoriza publicar, integrar ni desplegar.
