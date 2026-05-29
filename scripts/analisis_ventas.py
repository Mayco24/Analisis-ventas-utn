
ventas = {
    "Enero": 50000,
    "Febrero": 80000,
    "Marzo": 100000
}

print("=== ANALISIS DE VENTAS ===")

ventas_totales = sum(ventas.values())
print("Ventas totales:", ventas_totales)

print("\nVentas por mes:")
for mes, monto in ventas.items():
    print(mes, ":", monto)

producto_mas_vendido = "Mouse"
print("\nProducto mas vendido:", producto_mas_vendido)
