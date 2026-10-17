# 06 — Implementación, push, auditoría y aceptación

## Circuito

**Gestor humano u orquestador** lee el harness y asigna CP con base exacta → **implementador** edita sólo la rama autorizada, prueba y commitea → **publica commit en rama autorizada** → **auditor independiente** lee CANON/RULES/STATE, misión y diff contra base; busca violaciones, reproduce verificaciones cuando es seguro y emite dictamen → **gestor** acepta o devuelve hallazgos → STATE registra resultado.

## Informe de implementación

`CP, repo, base SHA, branch, HEAD SHA, archivos, pruebas ejecutadas con exit code, entorno, cambios no incluidos, riesgos, push URL, rollback.` Nunca uses “tests OK” sin nombre y salida real.

## Checklist del auditor

- ¿Está la ref prometida y el SHA publicado en Git?
- ¿El diff toca sólo el alcance autorizado? ¿Agrega side effects o dependencias fuera de alcance?
- ¿SOURCE contradice CANON aunque pasen tests?
- ¿Las pruebas cubren borde y falla? ¿Resultados verificables?
- ¿Hay secretos, mutación de datos reales o archivos ignored peligrosos?
- ¿Se actualizó STATE sin confundir test con aceptación humana?
- ¿La estrategia de rollback es realista?

## Rechazo y reauditoría

Dictamen `RECHAZADO` con archivo/línea, incumplimiento y corrección requerida. El implementador vuelve al **mismo frente/checkpoint**, genera un SHA nuevo; el auditor examina ese SHA y el delta adicional. No permitir que el auditor arregle y autoapruebe en la misma revisión.

## Aceptación

Dictamen técnico `APROBADO` sólo con evidencias. **No equivale** a merge, deploy, conformidad funcional del product owner ni éxito en producción. La autoridad humana conserva las decisiones reservadas.
