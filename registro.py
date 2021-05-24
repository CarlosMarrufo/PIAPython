import re, shutil, os, json
from datetime import datetime
from clases import Participante

lista_datos = []
index_linea = 0
info_cargada = False
info_actualizada = True
primera_carga = True

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
        if bool(re.match('^[0-9]{1}$', to_do)): #Validar que la variable to_do sea un número del 0 al 9
            if to_do == "1":
                cargarInformacion()
            elif to_do == "2":
                registrarParticipante()
            elif to_do == "3":
                buscarParticipante()
            elif to_do == "4":
                modificarParticipante()
            elif to_do == "5":
                eliminarParticipante()
            elif to_do == "6":
                mostrarParticipantes()
            elif to_do == "7":
                actualizarCSV()
            elif to_do == "8":
                serializarCSV()
            elif to_do == "0":
                cerrarPrograma()
        else:
            print("*"*60)
            input('**Opción inválida Presiona ENTER para continuar...')
        
def cargarInformacion(): #Función para cargar la información del archivo
    global lista_datos
    global info_cargada
    global primera_carga
    try: #Comprobar si existe el archive
        archivo_datos = open('datos.csv', 'r')
        for linea in archivo_datos:
            datos = linea.strip()
            lista_datos.append(datos)
        info_cargada = True
        if primera_carga:
            input('**Se ha cargado el archivo de datos, presiona ENTER para ingresar al sistema...')
            primera_carga = False
        else: input('**Se ha cargado el archivo de datos, presiona ENTER para volver al menú principal...')
    except: #Si no existe el archivo
        archivo_datos = open('datos.csv', 'w')
        archivo_datos.write('Correo | Nombre | Nacimiento | Monto | Folio | Momento') #Crear cabecera del archivo
        info_cargada = True
        input("**Se ha creado un archivo de datos nuevo, presiona ENTER para volver al menú principal...")

def registrarParticipante(): #Función para regirar un participante
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

def buscarParticipante(): #Función para buscar un participante
    global lista_datos
    global info_cargada
    global index_linea
    while(True):
        if not info_cargada:
            input("**No se ha encontrado un archivo de datos, favor de actualizar la información...")
            return False
        correo = validarCorreo()
        if not correo:
            return False
        if index_linea == 0:
            input("**No se ha encontrado el correo en la base de datos, presiona ENTER para regresar al menú principal...")
            return False
        else:
            participante = darFormato(index_linea)
            print("*"*14+" Información de participante "+"*"*14)
            print(f'Correo: {participante[0]}\nNombre: {participante[1]}\nNacimiento: {participante[2]}\nMonto: {participante[3]}\nFolio: {participante[4]}\nMomento: {participante[5]}')
            input("**Preciona ENTER para volver al menú principal...")
        return False

def modificarParticipante(): #Función para modificar un participante
    global lista_datos
    global info_cargada
    global index_linea
    global info_actualizada
    while(True):
        if not info_cargada:
            input("**No se ha encontrado un archivo de datos, favor de actualizar la información...")
            return False
        correo = validarCorreo()
        if not correo:
            return False
        if index_linea == 0:
            input("**No se ha encontrado el correo en la base de datos, presiona ENTER para regresar al menú principal...")
            return False
        else:
            participante = darFormato(index_linea)
            print("*"*14+" Información de participante "+"*"*14)
            print(f'Correo: {participante[0]}\nNombre: {participante[1]}\nNacimiento: {participante[2]}\nMonto: {participante[3]}\nFolio: {participante[4]}\nMomento: {participante[5]}')
            print("**Ingresar los datos actualizados a continuación")
            nombre = validarNombre()
            nacimiento = validarNacimiento()
            registro = Participante(participante[0], nombre, nacimiento, participante[3], participante[4], datetime.strptime(participante[5], "%Y-%m-%d %H:%M"))
            lista_datos[index_linea] = (registro.registrarParticipante())
            info_actualizada = False
            input("**Se ha actualizado la información del participante, presiona ENTER para regresar al menú principal...")
        return False

def eliminarParticipante(): #Función para eliminar un participante
    global lista_datos
    global index_linea
    global info_cargada
    global info_actualizada
    while(True):
        if not info_cargada:
            input("**No se ha encontrado un archivo de datos, favor de actualizar la información...")
            return False
        correo = validarCorreo()
        if not correo:
            return False
        if index_linea == 0:
            input("**No se ha encontrado el correo en la base de datos, presiona ENTER para regresar al menú principal...")
            return False
        else:
            participante = darFormato(index_linea)
            print("*"*14+" Información de participante "+"*"*14)
            print(f'Correo: {participante[0]}\nNombre: {participante[1]}\nNacimiento: {participante[2]}\nMonto: {participante[3]}\nFolio: {participante[4]}\nMomento: {participante[5]}')
            to_do = 0
            while(True):
                to_do = input("**¿Deseas eliminar al participante? [1] Sí | [0] No: ")
                if bool(re.match('^[0-1]{1}$', to_do)): #Validar que la variable to_do sea un número del 0 al 1
                    if to_do == "1":
                        lista_datos.pop(index_linea)
                        info_actualizada = False
                        input("**Participante eliminado del registro, presiona ENTER para volver al menú principal...")
                        return False
                    elif to_do == "0":
                        return False
                else:
                    input("**Selección inválida, presiona ENTER para continuar...") 

def mostrarParticipantes(): #Función para mostrar un participante
    global lista_datos
    index_linea = 1
    correo, nombre, nacimiento, monto, folio, momento = darFormato(0)
    print("-"*122)
    print ("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(correo, nombre, nacimiento, monto, folio, momento))
    print("-"*122)
    for linea in range(len(lista_datos) -1):
        correo, nombre, nacimiento, monto, folio, momento = darFormato(index_linea)
        print ("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(correo, nombre, nacimiento, monto, folio, momento))
        index_linea += 1
        if index_linea % 25 == 0: #Cada 25 lineas, mostrará nuevamente la cabecera.
            correo, nombre, nacimiento, monto, folio, momento = darFormato(0)
            print("-"*122)
            print ("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(correo, nombre, nacimiento, monto, folio, momento))
            print("-"*122)
    input("**Presiona ENTER para regresar al menú principal...")
    return False

def actualizarCSV(): #Función para actualizar el CSV
    global info_cargada
    global info_actualizada
    global lista_datos
    while(True):
        if not info_cargada:
            input("**No se ha encontrado un archivo de datos, favor de actualizar la información...")
            return False
        if info_actualizada:
            input("**No se han encontrado modificaciones en el archivo de datos, presiona ENTER para volver al menú principal...")
            return False
        try:
            archivo = shutil.copy("datos.csv", "datos.bak")
            print("Creando copia de seguridad en (",archivo,")...")
            os.remove("datos.csv")
            print("Eliminando el archivo de datos...")
            nuevo_csv = open("datos.csv", "w")
            for registro in lista_datos:
                nuevo_csv.write(registro + "\n")
            print("Creando nuevo archivo de datos...")
            input("**Actualización de la información completada, presiona ENTER para regresar al menú principal...")
            info_actualizada = True
            return False
        except:
            input("Ha ocurrido un error al actualizar la información, presiona ENTER para regresar al menú principal...")
            return False

def serializarCSV(): #Función para serializar en JSON
    global info_cargada
    global lista_datos
    global info_cargada
    try:
        open("datos_json.json", "r")
        to_do = 0
        while(True):
            if not info_cargada:
                input("**No se ha encontrado un archivo de datos, favor de actualizar la información...")
                return False
            to_do = input("**Ya existe un archivo de datos json, ¿deseas remplazarlo? [1] Sí | [0] No: ")
            if bool(re.match('^[0-1]{1}$', to_do)): #Validar que la variable to_do sea un número del 0 al 1
                if to_do == "1":
                    crearJson()
                    return False
                elif to_do == "0":
                    input("**No se ha creado el archivo json, presiona ENTER para regrear al menú principal...")
                    return False
            else:
                input("**Selección inválida, presiona ENTER para continuar...")
    except:
        crearJson()

def cerrarPrograma(): #Función para salir del programa
    global info_actualizada
    if not info_actualizada: #Verificar si existen cambios en el archivo
        to_do = 0
        while(True):
            to_do = input("**Se han encontrado cambios en el archivo, ¿desea guardarlos? [1] Sí | [0] No: ")
            if bool(re.match('^[0-1]{1}$', to_do)): #Validar que la variable to_do sea un número del 0 al 1
                if to_do == "1":
                    actualizarCSV()
                    return False
                elif to_do == "0":
                    input("**Presiona ENTER para salir del sistema...")
                    exit()
            else:
                input("**Selección inválida, presiona ENTER para continuar...")
    input("**Presiona ENTER para salir del sistema...")
    exit()

def crearJson(): #Función para crear el archivo JSON
    global lista_datos
    json_data = {}
    json_data['Participantes'] = []
    index_linea = 1
    for registro in range(len(lista_datos) - 1):
        arreglo = lista_datos[index_linea].strip().split(" | ")
        arreglo_json = {
            'correo': f'{arreglo[0]}',
            'nombre': f'{arreglo[1]}',
            'nacimiento': f'{arreglo[2]}',
            'monto': f'{arreglo[3]}',
            'folio': f'{arreglo[4]}',
            'momento': f'{arreglo[5]}'
        }
        json_data['Participantes'].append(arreglo_json)
        index_linea += 1
    with open("datos_json.json", "w") as archivo_json:
        archivo_json.write(json.dumps(json_data, indent=4))
    input("**Se ha creado el archivo json correctamente, presiona ENTER para regrear al menú principal...")
                    
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

def validarNombre(): #Función para validar el nombre del participante y archivo
    valido = False
    nombre = ""
    while(valido == False):
        nombre = input(f'Ingresa el nombre del participante (No espacios en blanco, de 5 a 40 caracteres): ')
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

def asignarFolio(): #Función para asignar el último folio al usuario a registrar
    global lista_datos
    folio = 0
    if lista_datos[-1] == lista_datos[0]: #Si el ultimo registro de lista_datos es igual al primero, crear primer folio
        folio = 12345
    else: #Si no, incrementar +1 al ultimo folio
        folio = int(str(lista_datos[-1]).split(" | ")[4]) + 1
    return folio

def darFormato(index_linea): #Función para dar formato a un registro
    global lista_datos
    return (lista_datos[index_linea].strip().split(" | "))

def main(): #Función principal
    cargarInformacion()
    mostrarMenu()

main()