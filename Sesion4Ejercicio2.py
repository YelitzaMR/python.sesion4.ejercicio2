#Usaremos 2 variables de tipo entero para que el usuario establezca el rango de comparación.
#Además se incluye una lista de tipo entero para almacenar los números impares
numInicial= int (input('Por favor introduzca el número inicial: '))
numFinal= int (input('Por favor introduzca el número final: '))
miLista: [int]=[]
#se usa un while con una comparación or para asegurarnos que el usuario ingrese datos válidos
while (numInicial==numFinal) or (numInicial>=numFinal):
    print('El número inicial debe ser menor que el número final, intente de nuevo')
    numInicial= int (input('Por favor introduzca el número inicial: '))
    numFinal= int (input('Por favor introduzca el número final: '))
for i in range (numInicial, numFinal+1):
    if (i % 2!=0):
        miLista.append(i)
print('La lista de números impares es: ', (miLista))

