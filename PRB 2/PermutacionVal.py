# clase principal pruebas tecnicas programacion Python

# import ctypes

class permutaciones():
    
    # BEGIN
    def __init__(self):
        print("")
         #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXX
    def menu(self):
        var1 = input("Ingrese un numero mayor a 0 y menor que 10: ")
        resul_entero = int(var1)
        #LISTA DE ALMACENAMIENTO DE 1 HASTA EL N INGRESADO
        enteros = [] 
        #VARIABLE DE POSICION PARA EL LISTADO
        posi = int(var1)
        #VALIDACION QUE EL NUMERO CUMPLA LA REGLA DE ESTAR EN EL RANGO
        if resul_entero < 0 or resul_entero >  10 : 
            print("El numero "+ str(resul_entero)+" no cumple con la regla")
            quit()
        for x in  range(1,resul_entero):
            enteros.append(x)
            x+=1
            i=x
        
        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXX
        #CICLO PARA ALIMENTAR LA LISTA EN BASE AL PARAMETRO ENTERO INGRESADO
        def insLis(posi, lst, i):
            return lst[:i] + [posi] + lst[i:] # INSERTAR LOS DATOS INGRESADO EN LA LISTA PRINCIPAL EN LA LISTAVACIA PARA VALIDACION 
        # insLis (40, enteros,3)
        
        
        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXX      
        def potencia(condat):
        
            if len(condat) == 0:
                return [[]]
            r = potencia(condat[:-1])
            #CREAR LOS GRUPOS EN BASE A LOS NUMEROS DE LA LISTA DE ENTEROS
            rtapot =  r +[ s +[condat[ - 1]] for s in r] 
            # print(f"Gripo potencia:  {len(condat)}",rtapot)
            conver = ",".join(map(str,rtapot))
            print(f"Permutacion ({len(condat)}) debe retornar:  {conver}")
            return rtapot
            
            
        potencia(enteros)    
         
        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXX
        def com_list(condat, n):
            com = [s for s in potencia(condat) if len(s) == n]
            return com
        
        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXX       
        def insLis_multiple(posi, lst):
            listaConjunta= [insLis(posi, lst, i) for i in range(len(lst)+1 )]
            conver = ",".join(map(str,listaConjunta))
            # print(f"Permutacion ({len(listaConjunta)}) debe retornar:  {conver}")
            return listaConjunta
        
       
        lista = enteros
        insLis_multiple(posi,enteros)
        
         #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXX
        def permuta(condat):
            if len(condat) == 0:
                return [[]]
            return sum([insLis_multiple(condat[0], s)for s in permuta(condat[1:])],[])
        
        # permuta(enteros)
               
        
         #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXX
        def permutaciones(condat, n):
            return sum([permuta(s) for s in com_list(condat, n)],[])
                    
        # permutaciones(enteros,1)
        # print("Final",enteros)
  
Ter = permutaciones()
Ter.menu() 
#END
