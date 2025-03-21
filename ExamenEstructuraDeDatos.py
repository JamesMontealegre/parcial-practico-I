#Entregado Por: Jose Jaider Manrique Codigo ID: 408715
ubicaciones = ["Plaza Central", "Parque del perro", "Estación Universidades", "Museo de cali", "Universidad Unicatolica"]

ultimo_digito = 5  

if ultimo_digito % 2 == 0:
    seleccionadas = [ubicaciones[i] for i in range(0, len(ubicaciones), 2)]
else:
    seleccionadas = [ubicaciones[i] for i in range(1, len(ubicaciones), 2)]

print("Ruta con ubicaciones en índices impares:")
print("Ruta definida:")
for lugar in ubicaciones:
    print(lugar)

print("\nRecorriendo ruta de impares:")
print("Iniciando recorrido...")
for lugar in seleccionadas:
    print(f"Llegaste a: {lugar}")

print("\nFin del recorrido.")
