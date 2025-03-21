import time

class Nodo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None  

class RutaTransporte:
    
    def __init__(self, ubicaciones, codigo):
        self.codigo = codigo
        self.ultimo_digito = int(codigo[-1])
        self.indices_pares = self.ultimo_digito % 2 == 0
        self.primero = None 

        
        ubicaciones_filtradas = [ubicaciones[i] for i in range(len(ubicaciones)) if (i % 2 == 0) == self.indices_pares]

    
        self.construir_lista(ubicaciones_filtradas)

    def construir_lista(self, ubicaciones):
    
        if not ubicaciones:
            return

        self.primero = Nodo(ubicaciones[0])
        actual = self.primero
        for nombre in ubicaciones[1:]:
            actual.siguiente = Nodo(nombre)
            actual = actual.siguiente

    def mostrar_ruta(self):
        
        print(f"\n🚏 Ruta con ubicaciones en índices {'pares' if self.indices_pares else 'impares'}:")
        actual = self.primero
        while actual:
            print("📍", actual.nombre)
            actual = actual.siguiente

    def recorrer_ruta(self):
        
        print("\n🛣️ Recorrido de la ruta:")
        print("🚦 Iniciando recorrido...")
        time.sleep(1)

        actual = self.primero
        while actual:
            print(f"🛑 Llegaste a: {actual.nombre}")
            time.sleep(1)
            actual = actual.siguiente

        print("🏁 Fin del recorrido.")


ubicaciones = ["Avenida Central", "Calle 5", "Plaza Mayor", "Estación Norte", "Museo Nacional", "Parque Bolívar", "Universidad Central"]


codigo_usuario = "0013833"


ruta_transporte = RutaTransporte(ubicaciones, codigo_usuario)
ruta_transporte.mostrar_ruta()
ruta_transporte.recorrer_ruta()
