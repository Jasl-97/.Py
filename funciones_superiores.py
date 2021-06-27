def funcion__superior(funcion_param):
    print(funcion_param())

def decir_hola():
    return 'hola'
def decir_mundo():
    return "mundo"    

funcion__superior(decir_hola)
funcion__superior(decir_mundo)