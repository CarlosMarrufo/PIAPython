import re
from datetime import datetime
from clases import Participante

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
    global lista_datos
    try:
        archivo_datos = open('datos.csv', 'r')
        for linea in archivo_datos:
            datos = linea.strip()
            lista_datos.append(datos)
        print('**Se ha cargado el archivo de datos')
    except:
        archivo_datos = open('datos.csv', 'w')
        archivo_datos.write('Correo | Nombre | Nacimiento | Monto | Folio | Momento')
        input("**Se ha creado un archivo de datos nuevo, presiona ENTER para volver al menú")

def registrarParticipante():
    global lista_datos
    while(True):
        correo = input("Ingresa el correo electrónico (10 a 40 caracteres): ")
        if correo == "": #Comprobar si se ingresa o no un correo
            input("Presiona ENTER para regresar al menú principal...")
            return False
        elif len(correo) < 10 or len(correo) > 40: #Comprobar si el correo está dentro del rango de caracteres
            input("El correo ingresado está fuera del rango de caracteres, presiona ENTER para continuar...")
        else:
            if validarCorreo(correo): #Validar el correo
                if correo in lista_datos: #Revisar si el correo ya está registrado
                    input("El correo ingresado ya está registrado, presiona ENTER para regresar al menú principal...")
                    return False
                else:
                    nombre = validarNombre()
                    nacimiento = validarNacimiento()
                    monto = input("Ingrese la aportación (cantidad monetaria): ")
                    folio = asignarFolio()
                    return False #Terminar while SOLO PARA TEST
            else:
                input("El correo ingresado no es válido, presiona ENTER para regresar al menú...")
                return False

def validarCorreo(correo): #Función para revisar si el correo ingresado es valido
    regular_exp = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(regular_exp, correo) is not None

def validarNombre(): #Función para validar el nombre
    valido = False
    nombre = ""
    while(valido == False):
        nombre = input("Ingresa el nombre del participante (No espacios en blanco, de 5 a 40 caracteres): ")
        if len(nombre) < 5 or len(nombre) > 40: #Validar cantidad de caracteres
            input("El nombre ingresado está fuera del rango de caracteres, presiona ENTER para continuar...")
        elif " " in nombre: #Validar que no contenga espacios
            input("El nombre ingresado contiene espacios, presiona ENTER para continuar...")
        else:
            valido = True
    return nombre
def validarNacimiento(): #Función para comprobar si la fecha de nacimiento es válida
    valido = False
    nacimiento = ""
    while(valido == False):
        nacimiento = input("Ingresa la fecha de nacimiento (YYYY-MM-DD): ")
        try: #Es válido
            datetime.strptime(nacimiento, '%Y-%m-%d')
            valido = True
        except: #Es inválido
            input("La fecha de nacimiento no es válida, comprueba el formato. Presiona ENTER para continuar...")
    return nacimiento            

def asignarFolio():
    global lista_datos
    print(lista_datos[0])

def main(): #Función principal
    mostrarMenu()

main()