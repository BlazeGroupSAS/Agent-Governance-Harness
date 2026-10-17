# Demostración — lista de tareas mínima

Ejemplo ficticio de un cambio `CP-001`: permitir que una función devuelva una lista nueva con una tarea agregada, rechazando títulos vacíos. Se implementa sin base de datos, sin servicios y con Python estándar.

## Secuencia end-to-end simulada (evidencia reproducible)

1. **Necesidad:** «Quiero agregar una tarea sin perder las existentes».
2. **Decisión de producto:** el CANON establece título no vacío, estado `pendiente` y ausencia de mutación de la lista inicial.
3. **STATE inicial:** F01 `NO_IMPLEMENTADO`, CP-001 previsto.
4. **Checkpoint:** [checkpoint-ejemplo.md](checkpoint-ejemplo.md) autoriza sólo `tareas.py` y `test_tareas.py`.
5. **Implementación candidata:** [tareas.py](tareas.py) más tests.
6. **Prueba local:** `python -m unittest -v`.
7. **Rechazo ilustrativo:** un auditor detecta que la primera revisión ficticia permitía `"   "` como título y emite `RECHAZADO`; no se representa ese error como un commit real.
8. **Corrección:** la versión actual valida `titulo.strip()` y conserva lista original.
9. **Reauditoría ilustrativa:** `APROBADO` si tests y lectura de fuente confirman invariantes. El dictamen en [auditoria-ejemplo.md](auditoria-ejemplo.md) es **didáctico**, no certificación de un auditor externo.
10. **STATE final ilustrativo:** [STATE.md](STATE.md) muestra cómo documentar el cierre. No afirma haber ejecutado un push/PR real.

## Ejecutar

```bash
cd examples/proyecto-demostracion
python -m unittest -v
```

**Importante:** no hay commit ni push demostrativo verdadero en este paquete. Los SHA de una gestión real se completan sobre el repositorio del lector; nunca inventarlos.
