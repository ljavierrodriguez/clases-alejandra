""" Ciclos o Bucles """
""" 

for in :

while


"""

for i in range(1, 11): # start = 0, stop = 5, step = 1 
    print(i)
    
i = 1
while i <= 10:
    print(i)
    i+=1  # i = i + 1
    

notas = [10, 23, 8, 32, 45, 90, 100, 12, 30, 19]
status = ("activo", "inactivo", "completado", "suspendido", "cancelado", "eliminado")
frutas = {"manzanas", "peras", "uvas"}


print(notas[5])
print(status[0])
print(frutas)

for i in range(len(notas)):
    print(notas[i])
    
for nota in notas:
    print(nota)
    
i = 0
while i < len(notas):
    print(notas[i])
    i = i + 1
