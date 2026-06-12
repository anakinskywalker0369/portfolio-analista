# portfolio-analista
# Automatizador Inteligente de Reportes de Ventas

Este proyecto es una herramienta diseñada para optimizar el análisis de datos de ventas, eliminando la carga operativa de limpiar y procesar archivos manualmente.

## 🛠 Problema resuelto
En entornos comerciales, los reportes suelen llegar con formatos inconsistentes, errores de escritura y datos faltantes. Procesar esta información en Excel manualmente consume horas de trabajo y es altamente propenso al error humano.

## 💡 Solución
He desarrollado un script en **Python** utilizando **Pandas** que:
1. **Limpia automáticamente:** Detecta y corrige errores de formato en precios y fechas.
2. **Gestiona valores nulos:** Elimina registros corruptos para asegurar la integridad del análisis.
3. **Genera resultados:** Crea un resumen estadístico y visualizaciones automáticas en segundos.

## 🚀 Tecnologías utilizadas
* **Python**
* **Pandas** (para manipulación de datos)
* **Matplotlib** (para visualización de gráficos)

## 📋 Cómo utilizarlo
1. Asegúrate de tener Python instalado y la librería pandas.
2. Ejecuta el script: `python CodigoAnalisis.py`.
3. Cuando el programa lo solicite, ingresa el nombre de tu archivo CSV.
4. El programa generará automáticamente un archivo `resumen_analisis.txt` y mostrará un gráfico de barras con el promedio de ventas.
