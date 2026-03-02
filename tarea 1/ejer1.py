class anime:
    def __init__(self,nombre,genero,nroEpisodios):
        self.nombre=nombre
        self.genero=genero
        self.__nroEpisodios=nroEpisodios
        self.__episodios=[]

class Televisor:
    def __init__(self,marca,resolucion,tipo):
        self.__marca=marca
        self.__resolucion=resolucion
        self.__tipo=tipo
    def __str__(self):
        return f"marca: {self.__marca}, resolucion: {self.__resolucion}, tipo: {self.__tipo}"
    
class Instrumento:
    def __init__(self,nombre,material,tipo):
        self.nombre = nombre
        self.__material = material
        self.__tipo = tipo
    def __str__(self):
        return f"nombre: {self.nombre}, material: {self.__material}, tipo: {self.__tipo}"        
    
    def getnombre(self):
        return self.nombre
    def getmaterial(self):
        return self.material
    def gettipo(self):
        return self.tipo
    
    def setnombre(self,nombre):
        selfnombre=nombre
    def setnombre(self,material):
        selfmaterial=material
    def setnombre(self,tipo):
        selftipo=tipo    

# Anime
a1 = anime("Naruto", "Shonen", 220)
a2 = anime("One Piece", "Aventura", 1000)

# Televisor
t1 = Televisor("Samsung", 4160, "OLED")
t2 = Televisor("Sony", 1080, "LED")

# Instrumento
i1 = Instrumento("Guitarra", "Madera", "Cuerda")
i2 = Instrumento("Flauta", "Metal", "Aire")

#no se imprime anime ya que no fue pedido en la UML
print("-----Televisor-----")
print(t1)
print(t2)
print("-----Instrumento-----")
print(i1)
print(i2)