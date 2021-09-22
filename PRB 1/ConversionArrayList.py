#clase principal pruebas tecnicas programacion Python

# import array
# import numpy
# from numpy import *
class pruebastecnicas:
# #begin
    def __init__calculo(self):
        print(" ")

    #ALGORITMO PARA ORDERNAR ASCENDENTE EL LISTADO
    def Calculo(self, valor):
        #
        tamañoVec=valor
        lista = []
        numDesc=input("Ingrese un numero desde el cual partir:") 
        for x in range(0,int(tamañoVec)):
            lista.append(int(numDesc))
            numDesc=int(numDesc)-1
 
        print(lista) # Imprimir en el orden que se encuentran
        lista.sort() # Asignar un urden ascendente a la lista
        print ("Lista" + str(lista))# Imprimir la lista en el orden correcto
        
        
        #ALGORITMO PARA ORDERNAR ASCENDENTE EL ARREGLO
    def calculo2(self,valor):
        tamañoVec=valor
        lista2 = [10,9,8,7,6,5,4,3,2,1]
        # lista2 = []
        numDesc=input("Ingrese un numero desde el cual partir el arreglo:") 
        for x in range(0,int(tamañoVec)):
            lista2[x] = int(numDesc)
            numDesc=int(numDesc)-1
    
            
        print("",lista2) # Imprimir en el orden que se encuentran
        lista2.sort() # Asignar un urden ascendente a la lista
        print ("Arreglo",lista2)# Imprimir la lista en el orden correcto
        
    

#end
#INICIALIZAR LA FUNCION DE LISTADO ASC
calculo =  pruebastecnicas()
valorIngresar= input("Ingrese un numero para el tamaño del vector: ")
calculo.Calculo(valorIngresar)

#INICIALIZAR LA FUNCION DEL ARREGLO ASC
valorIngresar2= input("Ingrese un numero para el tamaño del vector: ")
calculo.calculo2(valorIngresar2)