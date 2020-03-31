acum=0
limit= 250000*0.95        
limit_T=250000           

while acum < limit:
    peso = int(input("Ingrese el peso del paquete a enviar, en kilogramos:  "))
    
    #Evitar que reciba el proximo paquete, si este llegara a superar la capicidad maxima del avión.
    if acum + peso > limit_T:
        print("No podemos aceptar su paquete, pues superará el límite.")
        continue 
    else:

        if peso < 10:
            print("El peso no es aceptable")
            continue
        
        ds = int(input("Ingrese la distancia del viaje en kilómetros:  "))
        tv= input("¿El viaje es nacional o intercontinental?\n")

        #Evitar error del tipo de viaje
        if (tv != "nacional") or (tv != "intercontinental"):
            print("Error al ingresar el tipo de viaje.")
            while (tv != "nacional") and (tv != "intercontinental"):
                tv=input("Por favor vuelva a ingresar el tipo de vuelo.\n")
        tv = tv.lower

        #Evaluar condiciones y hallar el precio del envío
        if (tv == "nacional") and (peso > 100):
            precio = (peso*4500+ds*4000) * 0.85
        elif tv == "nacional":
            precio=(peso*4500+ds*4000)
        elif (tv == "intercontinental") and (ds > 8000) and (peso > 400):
            precio=(peso*4500+(ds*0.6213) *8000) *0.9
        else:
            precio=(peso*4500+(ds*0.6213) *8000)
    
    print("El costo del envío es de $",precio,"COP") 
    acum = peso + acum

print("No se pueden recibir más paquetes.")