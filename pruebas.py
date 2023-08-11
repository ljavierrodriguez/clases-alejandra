def obtenerDatos():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    return a, b, c 


a, b, c = obtenerDatos()

print(a)
print(c)
print(b)


class Lampara:
    color = None
    size = None
    
    def changeColor():
        pass   
    
    
class Persona:
    nombre = None
    apellido = None
    direccion = None
    rut = None
    
    def caminar():
        pass
    
    def correr():
        pass
    
    def comer():
        print("Persona: Comiendo")
    

objAle = Persona()

objLuis = Persona()


print(objAle.comer())
print(objLuis.caminar())


class Estudiante(Persona):
    
    def comer():
        print("Estudiante: Comiendo")



objEstAle = Estudiante()
print(objEstAle.comer())


titulos = "Nombre,Apellido,Rut"
datos = titulos.strip().split(',') # ["Nombre", "Apellido", "Rut"]
titulo = datos[0]