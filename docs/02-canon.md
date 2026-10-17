# 02 — CANON: contrato de producto

CANON responde **qué debe ser** el producto, no qué hizo el último agente. Es la autoridad de producto aprobada por quien toma las decisiones.

## Qué registrar

- Propósito, usuarios y problema.
- Capacidades obligatorias y exclusiones explícitas.
- Reglas de negocio, invariantes y casos límite.
- Arquitectura y restricciones deliberadas, sólo las que son decisiones relevantes.
- Criterios globales de terminado y qué decisiones requieren autoridad humana.
- Contratos de evolución: qué queda fuera del MVP.

## Qué NO registrar

No pongas tareas por hacer, ramas, hashes efímeros, fecha del último test, porcentajes de avance, errores transitorios, PRs ni diario de reuniones. Eso vuelve inestable el contrato y debe ir a STATE o al historial Git. Tampoco justifiques una nueva regla de negocio porque el código actual ya la hace: primero se decide como producto.

## Ejemplo de regla verificable

> Una tarea creada aparece como pendiente. Marcarla completada cambia únicamente su estado; no altera título ni identificador.

Esto es mucho más verificable que «gestionar tareas fácilmente».

## Cambios de Canon

Ante una decisión nueva, detené cambios de comportamiento fuera del contrato. Documentá la cuestión, obtené autorización de producto, modificá CANON en cambio trazable y recién entonces rediseñá checkpoints y STATE. No confundas un comentario de agente con aceptación humana.

Plantilla: [CANON](../templates/.harness/CANON.md).
