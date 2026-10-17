# 05 — Checkpoints pequeños, verificables y reversibles

Un checkpoint debe poder auditarse sin reinterpretar el negocio. Si cambia producto, requiere decisión de producto; si cambia solamente implementación, debe mantener CANON.

## Contrato mínimo

- **ID / frente:** CP-001 en una gestión identificable.
- **Base Git:** repo, rama de partida y SHA completo; branch de destino.
- **Objetivo:** un cambio observable con referencia CANON/STATE.
- **Alcance permitido:** paths, comportamientos y exclusiones.
- **Precondiciones:** herramientas, permisos y entorno de test comprobados.
- **Pruebas:** comandos y resultados esperados; sin tocar DB real.
- **Aceptación:** invariantes, test focused + regresión relevante, diff limpio, reporte.
- **Rollback:** `git revert <sha>` para commit publicado, o descartar rama aislada sin merge; atención a migraciones de datos no reversibles.
- **Autorizaciones:** push a una rama específica no autoriza merge ni deploy.

## División correcta

En lugar de “hacer autenticación y usuarios”, usar: esquema aditivo → modelo → autorización → UI → hardening, cada unidad con su propio contrato. Evitar generar checkpoints por una línea trivial cuando comparten la misma condición de aceptación.

[Ejemplo concreto](../examples/proyecto-demostracion/checkpoint-ejemplo.md).
