# 03 — RULES: contrato de operación

RULES responde **cómo se autoriza y comprueba** el trabajo. Debe poder aplicarse por agentes distintos sin reexplicar cada sesión.

## Núcleo reutilizable

1. Leer CANON, RULES y STATE vigentes y confirmar la ref Git; no asumir main ni confiar en cachés de sesiones.
2. Identificar base SHA, rama y worktree; no alterar otra rama o proyecto.
3. Sólo modificar archivos autorizados; ampliar alcance implica nueva decisión.
4. No tocar producción, bases reales, credenciales ni servicios externos sin autorización específica.
5. Hacer preflight, focused tests y regresión pertinente; distinguir test ejecutado de supuesto.
6. Registrar pruebas y limitaciones; nunca afirmar que una validación ocurrió porque «debería pasar».
7. Commit trazable, push únicamente donde esté autorizado y auditoría independiente **sobre el commit publicado**.
8. Si falla auditoría: corregir dentro del mismo checkpoint, generar SHA nuevo, reenviar al auditor.
9. Actualizar STATE sobre hechos, preservar evidencias y separar aceptación técnica de validación humana.
10. HARD STOP ante contradicción de autoridad, riesgo destructivo, secreto expuesto o requisitos irresolubles.

## Reglas específicas del entorno

Stack, convenciones MVC, SQL, ejecución de pruebas, rutas protegidas o Graph se añaden en cada proyecto. No copies reglas PHP/MariaDB a un repositorio TypeScript sólo por fidelidad al origen.

## Verificación automática

Un validador puede detectar: Git en rama, estado dirty, diferencias con base, cambios fuera de alcance, marcadores de conflicto, sintaxis, resultados de scripts disponibles. **No demuestra** que el producto sea correcto, que nadie accedió a producción ni que una autorización humana exista. PASS mecánico no equivale a aprobación global.

Plantilla: [RULES](../templates/.harness/RULES.md).
