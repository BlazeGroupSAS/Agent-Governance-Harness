# Harness de Gobernanza para Agentes

**Gobernanza verificable para desarrollo de software asistido por agentes de IA.**

Kit educativo en castellano para proyectos que usan APX, Claude Code, Codex, Devin u otros agentes. Independiente del proveedor.

> Ejemplos ficticios y reproducibles; no contiene código privado de los proyectos estudiados.

## Cuatro fuentes, cuatro responsabilidades

| Archivo | Responsabilidad |
|---|---|
| `.harness/CANON.md` | Definir producto y decisiones que un agente no puede alterar unilateralmente |
| `.harness/RULES.md` | Establecer procedimientos, controles, permisos y pruebas |
| `.harness/STATE.md` | Registrar avance verificable, pendientes y evidencia |
| Graph (opcional) | Ayudar a localizar código; nunca reemplazarlo como autoridad |

## Empezar

1. Copiá las plantillas de `templates/.harness/` al repositorio del proyecto.
2. Escribí CANON con decisiones aprobadas por quien es responsable del producto.
3. Adaptá RULES a los permisos y herramientas efectivas.
4. Auditá el código y registrá en STATE solamente hechos comprobados.
5. Creá un checkpoint de alcance mínimo, con SHA base, pruebas, aceptación y rollback.
6. Implementá en una rama aislada, sin fusionar o publicar fuera de la autorización.
7. Encargá una auditoría independiente sobre el SHA y las pruebas reales.
8. Remediá lo rechazado, auditá de nuevo y actualizá STATE con evidencia.

## Guía

- [Introducción](docs/01-introduccion.md)
- [CANON](docs/02-canon.md)
- [RULES](docs/03-rules.md)
- [STATE](docs/04-state.md)
- [Checkpoints](docs/05-checkpoints.md)
- [Implementación y auditoría](docs/06-implementacion-y-auditoria.md)
- [Continuidad entre agentes](docs/07-continuidad-entre-agentes.md)
- [Graph opcional](docs/08-graph-opcional.md)

[Ejemplo ficticio reproducible](examples/proyecto-demostracion/README.md).

## Alcance y limitaciones

Los tests son evidencia acotada, no garantías universales. El harness no hace fiable a un agente por sí solo ni asegura ejecución autónoma. El Graph es derivado y puede ser incompleto o estar desactualizado. No distribuimos el validador ni el grafo privados del proyecto estudiado como componentes genéricos.

**Licencia:** MIT; ver [LICENSE](LICENSE).
