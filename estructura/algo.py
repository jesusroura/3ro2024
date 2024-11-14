Frutas={"manzana":{"precio":1500}, "pera":{"precio":800}}
#inicia el total
total = 0
totalCompra = 0
while True:
    #solicitamos al usuario la fruta que quiera comprar y su cantidad
    fruta=input("ingrese la fruta que desea vender:")
    cant=float(input("ingrese la cantidad a vender: "))
    #verficamos si la fruta esta en el diccionario
    if fruta in Frutas:
        #se calcula el total
        total=Frutas[fruta]["precio"] + cant
        totalCompra=totalCompra+total
        print(f"El total a pagar por {cant} kilos de {fruta} es: {total}")
        print("el precio de ",cant,"kg","de ",fruta, "es de:",total)
    else:
      print("la fruta ingresada no existe en el diccionario")
      respuesta=input("desea comprar otro producto si/no: ")
      if respuesta=="no":
        break
      print("el total de la compra es ",totalCompra)