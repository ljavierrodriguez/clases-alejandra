""" Funciones """

""" 

def nombre_func():
    sentencias

nombre_func = lambda params : sentencia

"""

""" Definicion de la funcion """
def saludo():
    print("Hola Alejandra")
    
""" Ejecucion """
saludo()

def sumar(a, b):
    print(a + b)
    return a + b
    
resultado = sumar(10, 10)
print(resultado)

restar = lambda a, b : a - b

resultado = restar(15, 3)
print(resultado)


mis_notas = [10, 23, 8, 32, 45, 90, 100, 12, 30, 19]
status = ("activo", "inactivo", "completado", "suspendido", "cancelado", "eliminado")
frutas = {"manzanas", "peras", "uvas"}

def mostrar_datos(arreglo):
    for valor in arreglo:
        print(valor)
        
mostrar_datos(mis_notas)
mostrar_datos(status)
mostrar_datos(frutas)

def status_pares(valores):
    for i in range(len(valores)):
        if i % 2 == 0:
            print(valores[i])
            
status_pares(status)


resultado = list(filter(lambda s: s == "activo", status))
print(resultado)