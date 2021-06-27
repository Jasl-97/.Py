
import pandas as pd 

def get_data():
    return pd.read_csv('agenda.csv')    

def show_menu():
    print(""" Opciones \n1. Crear \n2. Listar \n3. Buscar \n4. Editar \n5. Eliminar \n6. Salir """)
    option = input('Digite la opción: ')
    if option == '1':
        create()
    elif option == '2':
        list_contact()
    elif option == '3':    
        search()
    elif option == '4':
        update()
    elif option == '5':
        delete()        
    elif option == '7':
        exit()

def create():
    name, phone, email = input('Nombre: '), input('Celular: '), input('Email: ')
    filer = open('agenda.csv','a')
    filer.write(f'{name},{phone},{email}\n')
    filer.close()
def update():
    list_contact()
    id = int(input('Id de contacto: '))
    option= input(""" ¿Qué desea editar? \n1. Nombre\n2. Celular\n3. Email\n == > """)
    dataf = get_data()
    if option == '1':
        dataf.loc[id, 'nombre'] = input ('Nombre: ')
    elif option == '2':
        dataf.loc[id, 'celular'] = input ('Celular :')
    elif option == '3':
        dataf.loc[id, 'email'] = input ('Email: ')
    dataf.to_csv('agenda.csv', index=False)
    
def delete():
    list_contact()
    id= int(input('Id de contacto: '))
    dataf= get_data()
    dataf.drop([id], inplace=True,axis=0)
    dataf.to_csv('agenda.csv', index=False)

def search():
    name = input("Digita el nombre que deseas buscar: ")
    dataf = get_data()
    print( dataf[dataf['nombre'].str.contains(name)] )

def list_contact():
    print(get_data())

def run():
    show_menu()
    run()

if __name__ == '__main__':
    run()