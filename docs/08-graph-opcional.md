# 08 — Graph opcional: índice técnico, no autoridad

En el proyecto de referencia se utilizó **TechnicalGraph**, un extractor estático con JSON de nodos/relaciones, evidencia archivo:línea, consulta CLI, diagnósticos, validación y fingerprint de fuentes. Estas capacidades están documentadas en su README técnico, pero no se copia ni distribuye aquí su implementación privada.

## Cuándo aporta

Muchos controladores, modelos, rutas, tablas o dependencias difíciles de localizar. Un Graph bien generado permite buscar vecindarios e identificar archivos para inspección.

## Cuándo NO aporta

Proyecto pequeño, pocas rutas, o cuando mantener el extractor cuesta más que leer los archivos. Tampoco sirve si la cobertura es incompleta o el mapa está desactualizado.

## Límites del enfoque estático

- Un índice no comprende reglas de negocio ni reemplaza CANON.
- No garantiza capturar llamadas dinámicas, SQL armado en runtime, reflection o resoluciones de tipo ambiguas.
- Debe verificarse su frescura contra SOURCE antes de usarlo.
- Un cambio de sistema puede exigir regenerar el índice; si el extractor no alcanza una nueva estructura, documentá el gap y no inventes relaciones.

## Estado de esta distribución

**No hay módulo ejecutable Graph ni generador incluido.** Integrarlo es trabajo opcional posterior con autorización de publicación de código, fixtures ficticias y validación de determinismo/portabilidad.
