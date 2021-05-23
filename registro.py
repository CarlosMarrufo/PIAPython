import re
from datetime import datetime
from clases import Participante

lista_datos = []
index_linea = 0
info_cargada = False
info_actualizada = True

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
                buscarParticipante()
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
            input('**Opción inválida Presiona ENTER para continuar...')
        
def cargarInformacion():
    global lista_datos
    global info_cargada
    try:
        archivo_datos = open('datos.csv', 'r')
        for linea in archivo_datos:
            datos = linea.strip()
            lista_datos.append(datos)
        asignarFolio()
        info_cargada = True
        input('**Se ha cargado el archivo de datos, presiona ENTER para volver al menú principal...')
    except:
        archivo_datos = open('datos.csv', 'w')
        archivo_datos.write('Correo | Nombre | Nacimiento | Monto | Folio | Momento')
        info_cargada = True
        input("**Se ha creado un archivo de datos nuevo, presiona ENTER para volver al menú principal...")

def registrarParticipante():
    global lista_datos
    global index_linea
    global info_actualizada
    global info_cargada
    index_linea = 0
    while(True):
        if not info_cargada: 
            input("**No se ha encontrado un archivo de datos, favor de actualizar la información...")
            return False
        correo = validarCorreo()
        if index_linea > 0:
            input("**El correo ingresado ya se encuentra registrado, presiona ENTER para continuar...")
        elif correo:
            nombre = validarNombre()
            nacimiento = validarNacimiento()
            monto = input("Ingrese la aportación (cantidad monetaria): ")
            folio = asignarFolio()
            registro = Participante(correo, nombre, nacimiento, monto, folio)
            lista_datos.append(registro.registrarParticipante())
            info_actualizada = False
            input(f'**Se ha registrado el participante {nombre.upper()} con el folio {folio}, presiona ENTER para volver al menú principal...')
            return False
        else:
            return False

def buscarParticipante():
    global lista_datos
    global info_cargada
    global index_linea
    while(True):
        if not info_cargada:
            input("**No se ha encontrado un archivo de datos, favor de actualizar la información...")
            return False
        correo = validarCorreo()
        if index_linea == 0:
            input("**No se ha encontrado el correo en la base de datos, presiona ENTER para regresar al menú principal...")
        else:
            participante = darFormato(index_linea)
            print("*"*14+" Información de participante "+"*"*14)
            print(f'Correo: {participante[0]}\nNombre: {participante[1]}\nNacimiento: {participante[2]}\nMonto: {participante[3]}\nFolio: {participante[4]}\nMomento: {participante[5]}')
            input("**Preciona ENTER para volver al menú principal...")
        return False

def validarCorreo(): #Función para validar el correo
    global index_linea
    valido = False
    correo = ""
    while(valido == False):
        correo = input("Ingresa el correo electrónico (10 a 40 caracteres): ")
        if correo == "": #Comprobar si se ingresa o no un correo
            input("**Presiona ENTER para regresar al menú principal...")
            index_linea = 0
            return False
        elif len(correo) < 10 or len(correo) > 40: #Comprobar si el correo está dentro del rango de caracteres
            input("**El correo ingresado está fuera del rango de caracteres, presiona ENTER para continuar...")
        elif formatoCorreo(correo):
            index_linea = 0
            for participante in lista_datos:
                if correo in participante:
                    correo = ""
                    return index_linea
                index_linea += 1
            index_linea = 0
            valido = True
        else:
            input("**El correo ingresado no es válido, presiona ENTER para regresar al menú principal...")
            return False
    return correo
    
def formatoCorreo(correo): #Función para revisar si el correo ingresado es valido
    regular_exp = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(regular_exp, correo) is not None

def validarNombre(): #Función para validar el nombre
    valido = False
    nombre = ""
    while(valido == False):
        nombre = input("Ingresa el nombre del participante (No espacios en blanco, de 5 a 40 caracteres): ")
        if len(nombre) < 5 or len(nombre) > 40: #Validar cantidad de caracteres
            input("**El nombre ingresado está fuera del rango de caracteres, presiona ENTER para continuar...")
        elif " " in nombre: #Validar que no contenga espacios
            input("**El nombre ingresado contiene espacios, presiona ENTER para continuar...")
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
            input("**La fecha de nacimiento no es válida, comprueba el formato. Presiona ENTER para continuar...")
    return nacimiento            

def asignarFolio():
    global lista_datos
    folio = 0
    if lista_datos[-1] == lista_datos[0]:
        folio = 12345
    else:
        folio = int(str(lista_datos[-1]).split(" | ")[4])
    return folio

def darFormato(index_linea): #Función para dar formato a un registro
    global lista_datos
    return (lista_datos[index_linea].strip().split(" | "))

def main(): #Función principal
    mostrarMenu()

main()