class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad      
        self.pasajeros = 0              
        self.ingresos = 0.0            
   
    def subir_pasajeros(self, cantidad):
        if cantidad <= 0:
            print("Cantidad de pasajeros inválida.")
            return
        if self.pasajeros + cantidad > self.capacidad:
            print(f"No hay suficientes asientos. Solo pueden subir {self.capacidad - self.pasajeros} pasajeros.")
        else:
            self.pasajeros += cantidad
            print(f"{cantidad} pasajeros subieron al bus. Total pasajeros: {self.pasajeros}")

 
    def cobrar_pasaje(self, costo=1.50):
        total = self.pasajeros * costo
        self.ingresos += total
        print(f"Se cobró Bs. {total:.2f} por {self.pasajeros} pasajeros.")

 
    def asientos_disponibles(self):
        disponibles = self.capacidad - self.pasajeros
        print(f"Asientos disponibles: {disponibles}")
        return disponibles

mi_bus = Bus(40)


mi_bus.subir_pasajeros(25)


mi_bus.cobrar_pasaje()

mi_bus.asientos_disponibles()

mi_bus.subir_pasajeros(20) 