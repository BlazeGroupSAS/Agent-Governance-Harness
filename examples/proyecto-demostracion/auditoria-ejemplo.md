# Auditoría didáctica CP-001

**No es una auditoría independiente realmente ejecutada sobre GitHub.** Es un modelo de informe que el lector puede reproducir.

## Ronda 1 — RECHAZADO (escenario ficticio)

- **Hallazgo:** candidato hipotético aceptaba título `"   "`.
- **Contrato:** CANON exige que `strip()` no quede vacío.
- **Acción:** devolver al implementador, agregar validación y test de blancos.

## Ronda 2 — Condición de APROBADO (sobre versión distribuida)

- Revisión de `tareas.py` muestra verificación de `titulo.strip()` y construcción de nueva lista.
- `test_tareas.py` cubre creación, inmutabilidad, blanco, tipo inválido y lista inválida.
- Dictamen se emite sólo tras ejecutar pruebas realmente y registrar resultado/exit code en el entorno usado.
- No equivale a aprobación humana, merge ni deploy.
