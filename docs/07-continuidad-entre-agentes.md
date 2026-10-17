# 07 — Continuidad al cerrar sesión o cambiar agente

La memoria conversacional es auxiliar. La continuidad confiable sale de **Git + CANON + RULES + STATE + misión vigente + evidencia externa**.

## Protocolo de reingreso

1. Identificá repo, rama, SHA y cambios locales pendientes; no presupongas que main es la última versión.
2. Leé CANON y RULES efectivos y recargá STATE. Si mantenés caché, invalidala al cambiar blob Git o detectar modificaciones staged/unstaged; STATE se recarga siempre.
3. Encontrá el frente, checkpoint abierto, permiso de push/merge y actor responsable.
4. Revisá el último informe de implementación/auditoría y confirmá que el SHA aún coincide.
5. Si hay trabajo incompleto, continuá **la misma misión**; no crear otra para “asegurar” una delegación pendiente.
6. Antes de informar cierre, corroborá pruebas y dictamen.

## APX y otros orquestadores

APX puede aportar actores, frentes, delegación y wake según versión/configuración. Claude Code, Codex y Devin pueden emplear el mismo contrato documental sin compartir semántica de sesiones. No prometemos idempotencia de ejecución ni wake automáticamente: una política de no duplicar delegaciones no prueba exclusión de carreras.

## Paquete mínimo de handoff

```text
Proyecto: demo-tareas
Frente: alta-tareas
Checkpoint: CP-001
Base: <SHA>
HEAD candidato: <SHA>
Estado: IMPLEMENTADO_PENDIENTE_AUDITORIA
Autorización: push rama cp/001, no merge
Evidencia: comando + exit code + salida
Próxima acción: auditor revisa diff base..HEAD
```

Nunca transferir credenciales o transcript completo como sustituto de esa ficha.
