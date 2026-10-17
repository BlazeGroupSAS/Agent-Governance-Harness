# 04 — STATE: continuidad verificable

STATE contesta qué está implementado, qué falta, qué contradice CANON y qué se debe hacer después. No es el lugar para reformular producto.

## Representación sugerida

Cada capacidad conserva ID estable, referencia CANON, alcance (`MVP` o `POST_MVP`), estado (`COMPLETO`, `PARCIAL`, `NO_IMPLEMENTADO`, `CONTRADICE_CANON`, `NO_APLICA_IMPLEMENTACION`), evidencias exactas, brecha y condición de cierre. La dimensión **alcance** es diferente de **estado**.

Evidencias distintas: SOURCE a una ref/SHA demuestra implementación; test demuestra sólo sus aserciones y su entorno; validación manual humana es otra cosa y debe declararse expresamente. Un índice Graph sólo ayuda a encontrar SOURCE.

## Cómo evitar un historial infinito

- **Arriba:** resumen operativo pequeño con HEAD verificado, bloqueos, siguiente CP y enlaces a evidencias.
- **En el medio:** inventario por capacidad estable; una línea de conclusión + links por capacidad.
- **Abajo o fuera:** decisiones históricas en commits, PR y `docs/decisiones/`; no pegar cada conversación.
- Después de cada CP, actualizar los ítems afectados y el próximo paso, compactando narraciones repetidas sin borrar evidencia vinculada.
- Si una evidencia envejece al cambiar SOURCE, marcarla pendiente de revalidación; no dejar un `COMPLETO` absoluto sin referencia.

## Regla de cierre

`COMPLETO` = suficiente implementación/evidencia técnica para **esa capacidad**, no aceptación manual de producto ni autorización de despliegue.

Plantilla: [STATE](../templates/.harness/STATE.md).
