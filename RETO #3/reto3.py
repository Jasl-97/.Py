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
    coordenadas=[["EMPTY" for i in range (3)] for j in range (2)]
    print("Debe ingresar las coordenadas con 3 cifras decimales separandolas con un punto")
    i=0
    for i in range (3): 
        print("Ingrese las coordenada "+ str(i+1))
        latitud=float(input("Ingrese la latitud ==> "))
        superior= float(2.766)
        inferior= float(2.548)
        oriente=float(-76.493)
        occidente=float(-76.879)
        if latitud <= superior and latitud >= inferior:
            coordenadas[0] [i]=str(latitud)
            longitud= float(input("Ingrese la longitud ==> "))
            if longitud <= oriente and latitud >=occidente:
                coordenadas[1] [i]= str(longitud)
                continue
            else:
                print("Error")      
        else:
            print("Error") 
            break
    print("La coordenada [latitud, longitud] 1 es: "+"["+"'"+str(coordenadas[0][0])+"'"+","+"'"+str(coordenadas[1][0])+"'"+"]" )
    print("La coordenada [latitud, longitud] 2 es: "+"["+"'"+str(coordenadas[0][1])+"'"+","+"'"+str(coordenadas[1][1])+"'"+"]" )
    print("La coordenada [latitud, longitud] 3 es: "+"["+"'"+str(coordenadas[0][2])+"'"+","+"'"+str(coordenadas[1][2])+"'"+"]" )

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
                    print("Usted ha elegido la opcion 1")
                    user_password=input("Ingrese la contraseña ==> ") # si el usuario es correcto pedimos la contraseña 
                    if user_password == password:
                        new_password= input("Ingrese la nueva contraseña ==> ")
                        if new_password == password:
                            print("Ingrese una contraseña diferente")
                            break
                        else:    
                             password= new_password
                        continue
                    else:
                         print("Error")
                    break
                elif opt == 2: #condicionales para ingresar a la opcion
                    print("Usted ha elegido la opcion 2")
                    coordenadas()
                elif opt == 3: #condicionales para ingresar a la opcion
                    print("Usted ha elegido la opcion 3")
                    break
                elif opt == 4: #condicionales para ingresar a la opcion
                    print("Usted ha elegido la opcion 4")
                    break
                elif opt == 5: #condicionales para ingresar a la opcion
                    print("Usted ha elegido la opcion 5")
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
                elif opt == 7: #condicionales para ingresar a la opcion
                    print("Hasta pronto")
                    break
                else:
                    print("Error")
                    count_error=count_error+1  #acumulador de errores                             
        else:
            print("Error")
            exit(0)
    else:
        print("Error")
        exit(0)
else:
    print("Error")
    exit(0)    