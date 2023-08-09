""" Condicionales """
""" 
Operadores de Comparacion

==
!=
>=
<=
>
<

Operadores Logicos

and, or, not

"""

""" 

if condicion:
    sentencia
    
if condicion:
    sentencia
else:
    sentencia
    
    
if condicion:
    sentencia
elif condicion:
    sentencia
else:
    sentencia

"""

a = 5
b = 6
c = 3
d = 9

if a > b:
    print(a)
    

if b > c:
    print(b)
else:
    print(c)
    
if a > b and a > c:
    print("El mayor es A")
elif b > c:
    print("El mayor es B")
else:
    print("El mayor es C")
    
    
if a > b or a > c or a > d:
    print("Ejecutando bloque A")
else:
    print("No puedo realizar ninguna tarea") 