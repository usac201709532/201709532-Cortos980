
def collatz(numero): # se define la funcion
    while numero != 1: #se ejecutara este ciclo hasta que se cumpla la condicion
        if numero % 2 == 0: # Se mira si el numero es par
            lista.append(int(numero)) #se guarda el dato en una lista
            numero = numero / 2 
        else:
            lista.append(int(numero)) #Sino espar, se guarda el dato al final de la llista
            numero = (numero * 3) + 1 #se hace la operacion 3N + 1

        if numero == 1:  #SI es numero es 1 es por que llego al final
            lista.append(1)  # se guarda un uno al final de la lista
        
lista=[]  
for i in range(2,12):
    collatz(i)
print(lista)  #se imprime la lista al final

lista1 = 'collatz.txt'

archivo = open(lista1, 'r')
for linea in archivo:
    registro = linea.split(',')
    datos.append(registro)
archivo.close()