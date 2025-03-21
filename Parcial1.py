import time

class RouteNode:
    """Nodo de la ruta que almacena una ubicación y la referencia al siguiente nodo."""
    def __init__(self, location):
        self.location = location
        self.next = None

class Route:
    def __init__(self):
        self.head = None

    def add_location(self, location):
        """Agrega una nueva ubicación al final de la ruta."""
        new_node = RouteNode(location)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def show_route(self):
        """Muestra la ruta completa."""
        current = self.head
        if not current:
            print("⚠️ No hay una ruta definida.")
            return

        print("📍 Ruta con ubicaciones en índices pares:\n")
        print("🛣️ Ruta definida:")
        while current is not None:
            print(f"➡️ {current.location}")
            current = current.next

    def navigate_route(self):
        """Simula el recorrido de la ruta con pausas entre ubicaciones."""
        current = self.head
        if not current:
            print("⚠️ No hay una ruta para navegar.")
            return

        print("\n🛰️ Recorriendo ruta de pares:")
        print("🚗 Iniciando recorrido...\n")

        def show_next_step(node):
            if not node:
                print("\n🏁 Fin del recorrido.")
                return
            time.sleep(1.5)
            print(f"🛑 Llegaste a: {node.location}")
            show_next_step(node.next)

        show_next_step(current)


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

if __name__ == "__main__":
    city_route = Route()

   
    for i in range(len(locations)):
        if i % 2 == 0:  # Índices pares
            city_route.add_location(locations[i])

    city_route.show_route()
    print("\n🔄 Simulación del recorrido en la ruta:\n")
    city_route.navigate_route()
