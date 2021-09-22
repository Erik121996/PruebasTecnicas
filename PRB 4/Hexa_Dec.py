
import array
import os

def convertir_a_hex():
    os.system('cls')
    lista = ['58A6', 'FC89', 'BD1A', '4313', '1250', '0F21', 'C89B', 'D1A4']
    lista2 = []
    for x in range(0,7,1):
        prb1 = lista[x]
        resul = int(prb1,16)     
        lista2.append(str(resul))
        pass
    
    print("lista ",lista)
    print("lista 2",lista2)
      
convertir_a_hex()


