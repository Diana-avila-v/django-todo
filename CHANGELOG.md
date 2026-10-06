\# CHANGELOG



\## \[v1.0.0] - 2026-10-06



\### Agregado

\- Pruebas de validación para el ingreso de títulos de tareas.

\- Pipeline de integración continua mediante GitHub Actions.

\- Archivo `requirements.txt` para la instalación de dependencias.

\- Generación del reporte de pruebas como artefacto del pipeline.



\### Corregido

\- Validación de títulos vacíos o compuestos únicamente por espacios al agregar una tarea.



\### Integración continua

\- Ejecución automática de `manage.py check`.

\- Aplicación de migraciones durante el pipeline.

\- Ejecución automatizada de las pruebas unitarias.

\- Generación del reporte de resultados de las pruebas.

