prod=[]
rta="si"
while rta=="si" or rta=="si" or rta=="si":#el while hace que se repita todas las veces que elija si
    opcion=input("seleccione una opcion \n 1.agregar productos a la lista \n 2-mostrar productos en la lista \n 3.salir")#aca le doy al usuario unas opciones para que elija
    if opcion=="1":#una opcion para el usuario
        productoAgregar=input("ingrese el nombre del producto a agregar a la lista: ")
        prod.append(productoAgregar)
    elif opcion=="2":#esta opcion muestra los producto que agrego o ya estaban 
        print("los productos que estan son:\n____________________")
        for p in prod:#este for muestra la lista ordenada
            print (p)
    elif opcion=="3":
        rta=input("esta seguro de salir del programa si\no: ")#aca le pregunto si esta seguro de salir
        if rta=="no" or rta=="NO" or rta=="NO":
            print("saliendo del programa")
    else:
        print("ingreso una opcion invalida")
    