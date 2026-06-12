import pandas as pd
import matplotlib.pyplot as plt
import os

def ejecutar_analisis():
    nombre = input("Ingresa el nombre del archivo CSV (ej: Ventas.csv): ")
    
    if not os.path.exists(nombre):
        print(f"Error: El archivo '{nombre}' no existe.")
        return

    try:
        # Carga
        df = pd.read_csv(nombre, encoding='latin-1', sep=';')
        
        # --- ETAPA DE LIMPIEZA AUTOMÁTICA ---
        print("\nLimpiando datos...")
        
        # 1. Convertir precios a números, convirtiendo errores en nulos (NaN)
        df['precio de venta S/'] = pd.to_numeric(df['precio de venta S/'], errors='coerce')
        
        # 2. Eliminar filas donde falta información crítica (Precio o Categoria)
        df = df.dropna(subset=['precio de venta S/', 'Categoria'])
        
        # 3. Convertir fechas a formato datetime
        df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
        
        print("¡Datos limpios y listos para analizar!")
        # -------------------------------------

        # Análisis
        resumen = df.groupby('Categoria')['precio de venta S/'].mean()
        
        reporte = f"--- REPORTE PROFESIONAL ---\n"
        reporte += f"Total de registros limpios: {len(df)}\n\n"
        reporte += "Promedio de ventas por categoría:\n"
        reporte += resumen.to_string()
        
        # Guardar resultado
        with open("resumen_analisis.txt", "w") as f:
            f.write(reporte)
        
        print(reporte)
        
        # Visualización
        resumen.plot(kind='bar', color='teal', edgecolor='black')
        plt.title(f'Ventas promedio por Categoría')
        plt.xlabel('Categoría')
        plt.ylabel('Precio Promedio (S/)')
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    ejecutar_analisis()
