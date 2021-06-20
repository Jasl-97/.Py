#Definimos el diccionario que llevara nuestro menu 
menu={'1': 'Cambiar contraseña', 
      '2': "Ingresar cordenadas actuales", 
      '3': "Ubicar zona wifi más cercana",
      '4': 'Guardad archivo con ubicación cercana', 
      '5': 'Actualizar registros de zonas wifi desde archivo',
      '6': 'Elegir opción de menú favorita',
      '7': 'Cerrar sesión'}
#Creamos una función que nos permita imprimir el menu      
def menu_print():
    for key in menu: #Recorremos el diccionario "menu" con un ciclo for
        print(key+"."+menu[key]) #imprimimos en pantalla cada clave con cada valor
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
user= "51743"   #se define una contraseña y un usuario
password="34715"
user_name= input(("Ingrese el nombre de usuario ==> ")) #capturamos la entrada del usuario
if user_name == user: #condicional para validar si el usuario es correcto de lo contrario imprimios error
    user_password=input("Ingrese la contraseña ==> ") # si el usuario es correcto pedimos la contraseña 
    if user_password == password:   #condicional para validar si la contraseña es correcta de lo contrario imprimimos error
        print("SOLVE CAPTCHA") #validacion mediante captcha
        captcha1=user[2:5] #extraemos los 3 ultimos valores de la variable de usuario para el captcha
        captcha2=int(user[-2])*(((((((5*3)-9)//1)*3)-10)*2)//4)//4 # operacion matematica para obtener el antepenultimo valor del usuario
        solve_true=int(captcha1)+captcha2
        solve_user=int(input("Resuelva la operación "+str(captcha1) + "+" + str(captcha2) + ":"))
        if solve_user == solve_true:
            print("Sesión iniciada")
            count_error=0
            while count_error <3:
                menu_print()
                opt=int(input("Elija una opción ==> "))
                if opt == 1:
                    print("Usted ha elegido la opcion 1")
                    break
                elif opt == 2:
                    print("Usted ha elegido la opcion 2")
                    break
                elif opt == 3:
                    print("Usted ha elegido la opcion 3")
                    break
                elif opt == 4:
                    print("Usted ha elegido la opcion 4")
                    break
                elif opt == 5:
                    print("Usted ha elegido la opcion 5")
                    break
                elif opt == 6:
                    opt_favorite=int(input("Seleccione opción favorita ==> "))
                    if opt_favorite <= 5 and opt_favorite > 0:
                        riddle_1= int(input("Para confirmar por favor responda: " + 
                        "Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es ==> "))
                        if riddle_1 == captcha2:
                            riddle_2= int(input("Para confirmar por favor responda: " + 
                            "Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es ==> ")) 
                            if riddle_2 == int(user[-1]):
                                print(str(opt_favorite)+"."+ menu[str(opt_favorite)])
                                del (menu[str(opt_favorite)])
                                continue
                            else:

                                print("Error")
                                count_error=count_error+1    
                        else:
                            print("Error")
                            count_error=count_error+1     
                    else: 
                        print("Error")
                        count_error=count_error+1
                elif opt == 7:
                    print("Hasta pronto")
                    break
                else:
                    print("Error")
                    count_error=count_error+1                                        
        else:
            print("Error")
            exit(0)
    else:
        print("Error")
        exit(0)
else:
    print("Error")
    exit(0)    