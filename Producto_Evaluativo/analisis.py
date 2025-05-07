import pandas as pd

# Leer el archivo
df = pd.read_csv("ventas_100k.csv")

# Asegurar tipos correctos
df['PRECIO'] = pd.to_numeric(df['PRECIO'], errors='coerce')
df['CANTIDAD'] = pd.to_numeric(df['CANTIDAD'], errors='coerce')
df['VALOR_VENTA'] = pd.to_numeric(df['VALOR_VENTA'], errors='coerce')
df['COMISION'] = pd.to_numeric(df['COMISION'], errors='coerce')
df['FECHA'] = pd.to_datetime(df['FECHA'], errors='coerce')

# Calcular columna adicional: utilidad
df['UTILIDAD'] = df['VALOR_VENTA'] * 0.95

# Agregar columnas MES y TRIMESTRE
df['MES'] = df['FECHA'].dt.month
df['TRIMESTRE'] = df['FECHA'].dt.to_period('Q')

# Filtrar ventas cerradas
cerradas = df[df['ESTADO'] == 'Cerrado']

# Crear lista de respuestas
respuestas = []

# --- RESPUESTAS ---
respuestas.append(f"1. Total de registros: {len(df)}")

respuestas.append(f"2. Ventas por estado:\n{df['ESTADO'].value_counts()}")

respuestas.append(f"3. Valor total de ventas: {df['VALOR_VENTA'].sum()}")

respuestas.append(f"4. Promedio de comisión por venta cerrada: {cerradas['COMISION'].mean()}")

respuestas.append(f"5. Ciudad con más ventas cerradas: {cerradas['CIUDAD'].value_counts().idxmax()}")

respuestas.append(f"6. Valor total de ventas por ciudad:\n{df.groupby('CIUDAD')['VALOR_VENTA'].sum()}")

respuestas.append(f"7. 5 productos más vendidos:\n{df['PRODUCTO'].value_counts().head(5)}")

respuestas.append(f"8. Total de productos únicos vendidos: {df['PRODUCTO'].nunique()}")

respuestas.append(f"9. Vendedor con más ventas cerradas: {cerradas['VENDEDOR'].value_counts().idxmax()}")

respuestas.append(f"10. Categoría con mayor ingreso total: {df.groupby('CATEGORIA')['VALOR_VENTA'].sum().idxmax()}")

# Venta más alta
venta_max = df[df['VALOR_VENTA'] == df['VALOR_VENTA'].max()]
respuestas.append(f"11. Venta más alta:\n{venta_max[['CLIENTE', 'VALOR_VENTA']]}")

# Ventas inválidas
invalidas = df[(df['VALOR_VENTA'] <= 0) | (df['COMISION'] <= 0)]
respuestas.append(f"12. Ventas inválidas (valor/comisión <= 0):\n{invalidas}")

# Media de ventas por mes
respuestas.append(f"13. Media de ventas por mes:\n{df.groupby('MES')['VALOR_VENTA'].mean()}")

# Mes con más ventas cerradas
respuestas.append(f"14. Mes con más ventas cerradas: {cerradas['MES'].value_counts().idxmax()}")

# Ventas por trimestre
respuestas.append(f"16. Ventas por trimestre:\n{df['TRIMESTRE'].value_counts()}")

# Productos vendidos en más de 3 ciudades
prod_ciud = df.groupby('PRODUCTO')['CIUDAD'].nunique()
respuestas.append(f"17. Productos vendidos en más de 3 ciudades:\n{prod_ciud[prod_ciud > 3]}")

# Duplicados
respuestas.append(f"18. Registros duplicados: {df.duplicated().sum()}")

# Nulos eliminados
df_limpio = df.dropna(subset=['CLIENTE', 'PRODUCTO', 'VALOR_VENTA'])
respuestas.append(f"19. Registros después de eliminar nulos: {len(df_limpio)}")

# Producto con mayor utilidad
respuestas.append(f"20. Producto con mayor utilidad:\n{df.groupby('PRODUCTO')['UTILIDAD'].sum().idxmax()}")

# --- GUARDAR REPORTE CON UTF-8-SIG ---
with open("reporte.txt", "w", encoding="utf-8-sig") as f:
    for linea in respuestas:
        f.write(str(linea) + "\n\n")

print("✅ Análisis completo. El reporte se guardó como 'reporte.txt'.")
