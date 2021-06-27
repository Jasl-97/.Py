#Mensaje de bienvenida
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

user= "51743"   #se define un usuario
password="34715" #Se define una contraseña

#Definimos el diccionario que llevara nuestro menu 
menu={'1': 'Cambiar contraseña', 
      '2': 'Ingresar cordenadas actuales', 
      '3': 'Ubicar zona wifi más cercana',
      '4': 'Guardad archivo con ubicación cercana', 
      '5': 'Actualizar registros de zonas wifi desde archivo',
      '6': 'Elegir opción de menú favorita',
      '7': 'Cerrar sesión'}

#Creamos una función que nos permita imprimir el menu      
def menu_print():
    for key in menu: #Recorremos el diccionario "menu" con un ciclo for
        print(key+"."+menu[key]) #imprimimos en pantalla cada clave con cada valor
     
#Creamos la funcion para guardar las coordenadas         
def coordenadas():
    coordenadas=[["EMPTY" for i in range (3)] for j in range (2)] # creamos la matriz 2x3 para almacenar las coordenadas 
    print("Debe ingresar las coordenadas con 3 cifras decimales separandolas con un punto") #especificamos como se debe introducir las coordenadas
    i=0
    for i in range (3): #recorremos la matriz 
        print("Ingrese las coordenada "+ str(i+1))  #solicitamos la primera coordenada
        latitud=float(input("Ingrese la latitud ==> ")) #solicitamos la latitud
        superior= float(2.766) ############################################
        inferior= float(2.548) #     establecemos los rangos permitidos   #
        oriente=float(-76.493) ############################################
        occidente=float(-76.879) ##########################################
        if latitud <= superior and latitud >= inferior: #verificamos si se encuentra entre los rangos 
            coordenadas[0] [i]=str(latitud) #guardamos la latitud en la columna 1 
            longitud= float(input("Ingrese la longitud ==> ")) # pedimos ingresar la longitud
            if longitud <= oriente and latitud >=occidente: # verificamos si se encuetra en los rangos permitidos
                coordenadas[1][i]= str(longitud) # guardamos la longitud en la columna 2 
                continue
            else:
                print("Error coordenada") # si la coordenada de longitud es incorrecta 
                exit(0)      
        else:
            print("Error coordenada") # si la coordenada de latitud es incorrecta
            exit(0)
    print("La coordenada [latitud, longitud] 1 es: "+"["+"'"+str(coordenadas[0][0])+"'"+","+"'"+str(coordenadas[1][0])+"'"+"]" )
    print("La coordenada [latitud, longitud] 2 es: "+"["+"'"+str(coordenadas[0][1])+"'"+","+"'"+str(coordenadas[1][1])+"'"+"]" )
    print("La coordenada [latitud, longitud] 3 es: "+"["+"'"+str(coordenadas[0][2])+"'"+","+"'"+str(coordenadas[1][2])+"'"+"]" )        
    #calculamos la coordenada mas al sur, para eso solo tenemos en cuneta la latitud pues esta involucra las cordenadas norte sur 
    menor=min(coordenadas[0]) # en la variable menor se guardamos la menor latitud de todas las almacenadas pues sera la que
    for i in range (3):       # este mas al norte, y recorremos cada una de las posiciones para saber cual fue la menor  
        if coordenadas[0][i] == menor:
            print("La coordenada "+str(i+1)+" es la que esta más al sur") # imprimimos en pantalla la ubicacion de la coordenada
    #calculamos la coordenada promedio entre los puntos
    latitud_promedio= (float(coordenadas[0][0])+float(coordenadas[0][1])+float(coordenadas[0][2]))/3 #promedio de latitud
    longitud_promedio=(float(coordenadas[1][0])+float(coordenadas[1][1])+float(coordenadas[1][2]))/3 #promedio de longitud
    print("La coordenada promedio de todos los puntos es "+"["+"'"+str(round(latitud_promedio,3))+
    "'"+"]"+","+"'"+str(round(longitud_promedio,3))+"'"+"]") #imprimimos la coordenada promedio de los puntos
    #actualizacion de coordenadas
    actualizar_coordenada=int(input("Presione 1, 2 o 3 para actualizar las respectivas coordenadas\n"
    +"presione 0 para regresar al menu ==>")) # pedimos ingresar la opcion para modificar las coordenadas
    if actualizar_coordenada!= 0 and actualizar_coordenada <= 3: # validamos la opcioni ingresada
        print("Debe ingresar las coordenadas con 3 cifras decimales separandolas con un punto") 
        latitud=float(input("Ingrese la latitud ==> ")) # pedimos la latitud
        if latitud <= superior and latitud >= inferior: # validamos con los rangos establecidos
            coordenadas[0][actualizar_coordenada-1]=str(latitud) # guardamos la coordenada actualizada
            longitud= float(input("Ingrese la longitud ==> ")) # pedimos la longitud
            if longitud <= oriente and latitud >=occidente: # validamos con los rangos establecidos
                coordenadas[1][actualizar_coordenada-1]= str(longitud) # guardamos la longitud actualizada 
            else:
                print("Error actualización") # si se ingresa una latitud incorrecta
                exit(0)      
        else:
            print("Error actualización") # si se ingresa una longitud incorrecta
            exit(0)
    print("La coordenada [latitud, longitud] 1 es: "+"["+"'"+str(coordenadas[0][0])+"'"+","+"'"+str(coordenadas[1][0])+"'"+"]" ) # imprimimos 
    print("La coordenada [latitud, longitud] 2 es: "+"["+"'"+str(coordenadas[0][1])+"'"+","+"'"+str(coordenadas[1][1])+"'"+"]" ) # las coordenadas
    print("La coordenada [latitud, longitud] 3 es: "+"["+"'"+str(coordenadas[0][2])+"'"+","+"'"+str(coordenadas[1][2])+"'"+"]" ) # actualizadas                         

#Condiciones de ingreso a la plataforma          
user_name= input(("Ingrese el nombre de usuario ==> ")) #capturamos la entrada del usuario
if user_name == user: #condicional para validar si el usuario es correcto de lo contrario imprimios error
    user_password=input("Ingrese la contraseña ==> ") # si el usuario es correcto pedimos la contraseña 
    if user_password == password:   #condicional para validar si la contraseña es correcta de lo contrario imprimimos error
        print("SOLVE CAPTCHA") #validacion mediante captcha
        captcha1=user[2:5] #extraemos los 3 ultimos valores de la variable de usuario para el captcha
        captcha2=int(user[-2])*(((((((5*3)-9)//1)*3)-10)*2)//4)//4 # operacion matematica para obtener el antepenultimo valor del usuario
        solve_true=int(captcha1)+captcha2 #respuesta verdadera de los captcha
        solve_user=int(input("Resuelva la operación "+str(captcha1) + "+" + str(captcha2) + ":")) #capturamos la solucion del usuario
        if solve_user == solve_true:#condicion para probar la solucion del captcha
            print("Sesión iniciada")
            count_error=0
            while count_error <3: #while para salir si se producen mas de 3 errores
                menu_print() #imprimimos el menu
                opt=int(input("Elija una opción ==> ")) #capturamos la opcion del usuario
                if opt == 1: #condicionales para ingresar a la opcion
                    print("Usted ha elegido la opción 1")
                    user_password=input("Ingrese la contraseña ==> ") # si el usuario es correcto pedimos la contraseña 
                    if user_password == password: #validamos si la contraseña es correcta
                        new_password= input("Ingrese la nueva contraseña ==> ") #solicitamos la nueva contraseña 
                        if new_password == password: # validamos si es diferente 
                            print("Ingrese una contraseña diferente") # solicitamos una nueva contraseña si esta es diferente
                            break
                        else:    
                             password= new_password # de lo contrario si es difente actualizamos la nueva contraseña
                        continue
                    else:
                         print("Error") # si la contraseña es incorrecta
                    break
                elif opt == 2: #condicionales para ingresar a la opcion
                    print("Usted ha elegido la opción 2")
                    coordenadas() # llamamos a la funcion de las coordenadas 
                elif opt == 3: #condicionales para ingresar a la opcion
                    print("Usted ha elegido la opción 3")
                    break
                elif opt == 4: #condicionales para ingresar a la opcion
                    print("Usted ha elegido la opción 4")
                    break
                elif opt == 5: #condicionales para ingresar a la opcion
                    print("Usted ha elegido la opción 5")
                    break
                elif opt == 6: #condicionales para ingresar a la opcion
                    opt_favorite=int(input("Seleccione opción favorita ==> ")) #capturamos la opcion favorita   
                    if opt_favorite <= 5 and opt_favorite > 0: # condicional para que la opcion solo sea entre las 5 primeras   
                        riddle_1= int(input("Para confirmar por favor responda: " + 
                        "Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es ==> ")) #la adivinanza 1
                        if riddle_1 == captcha2: #condicion para que la adivinanza 1
                            riddle_2= int(input("Para confirmar por favor responda: " + 
                            "Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es ==> ")) #adivinanza 2
                            if riddle_2 == int(user[-1]): #condicion para la adivinanza 2
                                print(str(opt_favorite)+"."+ menu[str(opt_favorite)]) #imprimimos la opcion favorita
                                del (menu[str(opt_favorite)]) # la borramos del menu
                                continue # continue para que imprima el menu
                            else:
                                print("Error")
                                count_error=count_error+1 #acumulador de errores
                        else:
                            print("Error")
                            count_error=count_error+1     #acumulador de errores
                    else: 
                        print("Error")
                        count_error=count_error+1   #acumulador de errores
                        exit(0)
                elif opt == 7: #condicionales para ingresar a la opcion
                    print("Hasta pronto")
                    break
                else:
                    print("Error")
                    count_error=count_error+1  #acumulador de errores                             
        else:
            print("Error") # si el captcha no es el coorecto
            exit(0)
    else:
        print("Error") # si la contraseña es incorrecta
        exit(0)
else:
    print("Error") # si el usuario es incorrecto
    exit(0)    