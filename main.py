import time

class RouteNode:
    def __init__(self, location):
        self.location = location
        self.next = None

class Route:
    def __init__(self):
        self.head = None

    def add_location(self, location):
        # Crear un nuevo nodo con la ubicación
        new_node = RouteNode(location)
        # Si la lista está vacía, hacer que el nodo sea la cabeza
        if not self.head:
            self.head = new_node
        else:
            # Si ya hay elementos, recorrer la lista hasta el final y agregar el nuevo nodo
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def show_route(self):
        current = self.head
        if not current:
            print("⚠️ No hay una ruta definida.")
            return
        print("🛣️ Ruta definida:")
        while current is not None:
            print(f"➡️ {current.location}")
            current = current.next

    def navigate_route(self):
        current = self.head
        if not current:
            print("⚠️ No hay una ruta para navegar.")
            return

        print("🚗 Iniciando recorrido...")

        def show_next_step(node):
            if not node:
                print("🏁 Fin del recorrido.")
                return
            time.sleep(1.5)
            print(f"🛑 Llegaste a: {node.location}")
            show_next_step(node.next)

        show_next_step(current)

# Lista de ubicaciones
locations = [
    "Avenida Central",
    "Calle 5",
    "Plaza Mayor",
    "Avenida del Río",
    "Estación Norte",
    "Parque Sur",
    "Museo Nacional",
    "Teatro Municipal",
    "Universidad Central",
    "Biblioteca Pública"
]

# Código de ejemplo: ruiz-000408330
codigo = "000408330"

# Determinar si el último dígito del código es par o impar
ultimo_digito = int(codigo[-1])  # Obtiene el último dígito del código
es_impar = ultimo_digito % 2 != 0

# Crear una nueva ruta
city_route = Route()

# Seleccionar las ubicaciones dependiendo de si el último dígito es par o impar
if es_impar:
    # Si el último dígito es impar, escoger las ubicaciones con índices impares
    print("Seleccionando ubicaciones con índices impares:")
    for i, location in enumerate(locations):
        if i % 2 != 0:
            city_route.add_location(location)
else:
    # Si el último dígito es par, escoger las ubicaciones con índices pares
    print("Seleccionando ubicaciones con índices pares:")
    for i, location in enumerate(locations):
        if i % 2 == 0:
            city_route.add_location(location)

# Mostrar la ruta definida
city_route.show_route()

# Simulación del recorrido
print("\n🔄 Simulación del recorrido en la ruta:\n")
city_route.navigate_route()

