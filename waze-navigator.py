# Python
# Edwin Yair Molina Cerón - 408873

import time

# Nodo de la ruta
class RouteNode:
    def __init__(self, location):
        self.location = location
        self.next = None

# Clase principal para manejar la ruta
class Route:
    def __init__(self):
        self.head = None

    # Método para agregar ubicaciones
    def add_location(self, location):
        new_node = RouteNode(location)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Mostrar la ruta
    def show_route(self):
        current = self.head
        if not current:
            print("⚠ No hay una ruta definida.")
            return
        print("🛣 Ruta definida:")
        while current:
            print(f"➡ {current.location}")
            current = current.next

    # Recorrer la ruta con pausas simuladas
    def navigate_route(self):
        current = self.head
        if not current:
            print("⚠ No hay una ruta para navegar.")
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

# Lista de ubicaciones disponibles
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

# Identificador de codigo par o impar
codigo = 408873
es_impar = codigo % 2 != 0  # True porque 3 es impar

if __name__ == "__main__":
    city_route = Route()

    # Agregar ubicaciones
    for i in range(len(locations)):
        if i % 2 != 0:  # Índices impares
            city_route.add_location(locations[i])

    # Mostrar la ruta definida
    city_route.show_route()

    # Simular el recorrido
    print("\n🔄 Simulación del recorrido en la ruta:\n")
    city_route.navigate_route()
