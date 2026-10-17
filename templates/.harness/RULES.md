# RULES — [Nombre del proyecto]

## 1. Autoridades
CANON define producto, RULES procedimiento, STATE evidencias y backlog, SOURCE comportamiento implementado. El owner resuelve ambigüedades de producto.

## 2. Preflight
Comprobar Git, base SHA, rama, clean/dirty, CANON, RULES y STATE efectivos. No asumir main ni estado de sesiones previas.

## 3. Scope
Trabajar sólo checkpoint autorizado. Cualquier ampliación material requiere nueva decisión.

## 4. Entornos
Nunca alterar producción ni datos reales para probar. Usar fixtures aislados y permisos específicos. No divulgar secretos.

## 5. Implementación
Rama aislada; focused tests y regresión relevante; informe con comandos, exit codes, cambios, riesgos y rollback. No inventar evidencias.

## 6. Git / publicación
Commit trazable y push sólo a refs autorizadas. Push no autoriza merge/deploy. No force push sin permiso explícito.

## 7. Auditoría
Auditor distinto del implementador, sin escribir/corregir durante revisión. Examina base..SHA publicado y requisitos, emite APROBADO/RECHAZADO con evidencias.

## 8. Corrección
RECHAZADO vuelve al implementador; misma gestión, nuevo SHA y nueva auditoría.

## 9. STATE
Actualización luego de evidencia comprobada. Completo técnico no equivale a aceptación humana.

## 10. HARD STOP
Suspender ante contradicción de CANON, permiso incierto, riesgo destructivo, secretos, o imposibilidad de validar condiciones obligatorias.

## 11. Condiciones específicas
[Agregar reglas de framework, migraciones, Graph o despliegue propias de este proyecto.]
