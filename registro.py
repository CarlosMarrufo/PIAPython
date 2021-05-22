import re
lista_datos = []
def mostrarMenu(): #Función para mostrar el menú principal
    while(True):
        print(22*"*"+" MENÚ PRINCIPAL "+"*"*22)
        print("[1] Cargar información de CSV")
        print("[2] Registrar participantes")
        print("[3] Buscar participante")
        print("[4] Modificar participante")
        print("[5] Eliminar participante")
        print("[6] Ver lista de participantes")
        print("[7] Actualizar información de CSV")
        print("[8] Serializar información a JSON")
        print("[0] Salir")
        to_do = input('¿Qué opción deseas?: ')
        if bool(re.match('^[0-9]{1}$', to_do)): #Validar que la variable toDo sea un número del 0 al 9
            if to_do == "1":
                cargarInformacion()
            elif to_do == "2":
                registrarParticipante()
            elif to_do == "3":
                pass
            elif to_do == "4":
                pass
            elif to_do == "5":
                pass
            elif to_do == "6":
                pass
            elif to_do == "7":
                pass
            elif to_do == "8":
                pass
            elif to_do == "0":
                break
        else:
            print("*"*60)
            input('Opción inválida Presiona ENTER para continuar...')
        
def cargarInformacion():
    try:
        archivo_datos = open('datos.csv', 'r')
        print('**Se ha cargado el archivo de datos')
    except:
        archivo_datos = open('datos.csv', 'w')
        archivo_datos.write('Folio | Correo | Nombre | Nacimiento | Momento')
        input("**Se ha creado un archivo de datos nuevo, presiona ENTER para volver al menú")

def registrarParticipante():
    registrado = 0
    while registrado == 0:
        correo = input("Ingresa el correo electrónico: ")
        print(validarCorreo(correo))
        registrado = 1

def validarCorreo(correo): #Función para validar si el correo ingresado es valido
    regular_exp = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(regular_exp, correo) is not None

def main(): #Función principal
    mostrarMenu()

main()