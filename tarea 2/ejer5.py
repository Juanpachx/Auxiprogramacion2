class Jugador:
    def __init__(self, nombre, diamantes):
        self.nombre = nombre
        self.diamantes = diamantes  

    def contar_stacks(self):
       
        stacks = self.diamantes // 64
        return stacks


class ServidorMinecraft:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.jugadores = []

   
    def agregar_jugador(self, jugador):
        if len(self.jugadores) >= self.capacidad:
            print(f"No se puede agregar a {jugador.nombre}, el servidor está lleno.")
        else:
            self.jugadores.append(jugador)
            print(f"{jugador.nombre} ha sido agregado al servidor.")
 
 
    def mostrar_stacks_por_jugador(self):
        print("Stacks de diamantes por jugador:")
        for jugador in self.jugadores:
            print(f"{jugador.nombre}: {jugador.contar_stacks()} stack(s)")


    def jugador_con_mas_diamantes(self):
        if not self.jugadores:
            print("No hay jugadores en el servidor.")
            return

        jugador_max = self.jugadores[0]
        for jugador in self.jugadores:
            if jugador.diamantes > jugador_max.diamantes:
                jugador_max = jugador

        print(f"El jugador con más diamantes es {jugador_max.nombre} con {jugador_max.diamantes} diamantes.")

    
    def total_diamantes(self):
        total = 0
        for jugador in self.jugadores:
            total += jugador.diamantes
        print(f"Total de diamantes en el servidor: {total}")
        return total

servidor = ServidorMinecraft(capacidad=10)


jugadores = [
    Jugador("Alex", 50),
    Jugador("Steve", 130),
    Jugador("Maya", 70),
    Jugador("Leo", 200),
    Jugador("Nina", 30),
    Jugador("Oscar", 64),
    Jugador("Sofia", 150),
    Jugador("Diego", 90),
    Jugador("Luna", 80),
    Jugador("Max", 10)
]


for jugador in jugadores:
    servidor.agregar_jugador(jugador)

servidor.mostrar_stacks_por_jugador()

servidor.jugador_con_mas_diamantes()

servidor.total_diamantes()