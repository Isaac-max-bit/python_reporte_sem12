import pandas as pd
import random
from faker import Faker
from datetime import datetime
import os

fake = Faker()

# Listas personalizadas
productos = ['Laptop', 'Celular', 'Tablet', 'Monitor', 'Impresora']
ciudades = ['Medellín', 'Bogotá', 'Cali', 'Barranquilla', 'Cartagena']
vendedores = ['Carlos Ruiz', 'Laura Gómez', 'Andrés Pérez', 'Sofía Martínez', 'Diego Torres']
estados = ['Cerrado', 'Pendiente', 'Cancelado']
categorias = ['Tecnología', 'Electrodoméstico', 'Accesorios']

# Crear datos
datos = []
for _ in range(100_000):
    cliente = fake.name()
    producto = random.choice(productos)
    precio = round(random.uniform(100_000, 3_000_000), 2)
    cantidad = random.randint(1, 10)
    ciudad = random.choice(ciudades)
    vendedor = random.choice(vendedores)
    fecha = fake.date_between(start_date='-1y', end_date='today')
    estado = random.choice(estados)
    valor_venta = round(precio * cantidad, 2)
    comision = round(valor_venta * 0.05, 2)
    categoria = random.choice(categorias)

    datos.append([
        cliente, producto, precio, cantidad, ciudad, vendedor,
        fecha, estado, valor_venta, comision, categoria
    ])

# Crear DataFrame
columnas = ['CLIENTE', 'PRODUCTO', 'PRECIO', 'CANTIDAD', 'CIUDAD', 'VENDEDOR',
            'FECHA', 'ESTADO', 'VALOR_VENTA', 'COMISION', 'CATEGORIA']
df = pd.DataFrame(datos, columns=columnas)

# Ruta al escritorio
ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop", "ventas_100k.csv")

# Guardar CSV
df.to_csv(ruta_escritorio, index=False)

print(f"Archivo guardado exitosamente en: {ruta_escritorio}")
