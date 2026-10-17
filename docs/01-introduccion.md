# 01 — Introducción

## Problema

Un agente puede completar una instrucción larga y aun así: elegir la rama equivocada, asumir requisitos, confundir código existente con producto deseado, inventar resultados, usar un test débil como prueba total o perder continuidad al cambiar de sesión. Un prompt no conserva automáticamente el contexto ni crea evidencia independiente.

## Modelo operativo

1. **Producto:** CANON define intención, fronteras y decisiones aprobadas.
2. **Procedimiento:** RULES fija permisos, obligaciones y condiciones de detención.
3. **Estado:** STATE registra lo observable y el backlog verificable.
4. **Unidad de trabajo:** checkpoint delimitado por base/ref, objetivo, restricciones, pruebas y rollback.
5. **Contraste:** auditor distinto al implementador compara código real contra contrato.
6. **Cierre:** sólo se cierra con dictamen, evidencia y documentación actualizada.

**Jerarquía práctica:** la autoridad humana decide producto y permisos; CANON especifica el producto aprobado; RULES controla el procedimiento; STATE describe evidencias y pendientes; SOURCE demuestra cómo se comporta el código actual. Si SOURCE contradice CANON, registrá el gap; no reescribas CANON para acomodar el código.

## No depende del número de agentes

Una sola persona con dos sesiones realmente separadas puede implementar y auditar. Si hay orquestador (por ejemplo, APX), puede delegar y recuperar respuestas. Eso no sustituye permisos Git ni validaciones reproducibles.

## Ruta de lectura

Personalizá las tres plantillas, estudiá [el checkpoint](05-checkpoints.md) y recorré [el ejemplo completo](../examples/proyecto-demostracion/README.md).
