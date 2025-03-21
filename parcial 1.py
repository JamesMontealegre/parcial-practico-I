import time

class RouteNode:
    def __init__(self, location):
        self.location = location
        self.next = None
    

class Route:
    def __init__(self):
        self.head = None

    def add_location(self, location):
        new_node = RouteNode(location)
        if not self.head:
            self.head = new_node
        else:
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
    user_code = input("Ingrese su código: ")
    last_digit = int(user_code[-1])

    city_route = Route()

    if last_digit % 2 == 0:
        selected_locations = [locations[i] for i in range(len(locations)) if i % 2 == 0]
    else:
        selected_locations = [locations[i] for i in range(len(locations)) if i % 2 != 0]

    for location in selected_locations:
        city_route.add_location(location)
    
    # Agregar rutas de manera iterativa dependiento de si su último número del código es par o impar

    city_route.show_route()

    print("\n🔄 Simulación del recorrido en la ruta:\n")
    city_route.navigate_route()