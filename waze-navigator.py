import time

class RouteNode:
    def __init__(self, location):
        self.location = location
        self.next = None

class Route:
    def __init__(self):
        self.head = None

    def add_location(self, location):
        current = self.head
        while current:
            if current.location == location:
                print(f"⚠️ Ubicación ya existe en la ruta: {location}")
                return
            current = current.next  

        new_node = RouteNode(location)
        if not self.head:  
            self.head = new_node
        else:  
            current = self.head
            while current.next is not None:
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
    city_route = Route()
    
    codigo = 2  #codigo para probrar
    ultimo_digito = int(str(codigo)[-1])  
    es_par = (ultimo_digito % 2 == 0)  


    for i, location in enumerate(locations):
        if (es_par and i % 2 == 0) or (not es_par and i % 2 != 0):
            city_route.add_location(location)  # Usar el método add_location para agregar la ubicación

    city_route.show_route()

    print("\n🔄 Simulación del recorrido en la ruta:\n")
    city_route.navigate_route()
