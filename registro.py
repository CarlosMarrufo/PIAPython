import re
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
        toDo = input('¿Qué opción deseas?: ')
        if bool(re.match('^[0-9]{1}$', toDo)):
            if toDo == "1":
                pass
            elif toDo == "2":
                pass
            elif toDo == "3":
                pass
            elif toDo == "4":
                pass
            elif toDo == "5":
                pass
            elif toDo == "6":
                pass
            elif toDo == "7":
                pass
            elif toDo == "8":
                pass
            elif toDo == "0":
                break
        else:
            print("*"*60)
            input('Opción inválida Presiona ENTER para continuar...')
        
        
def main(): #Función principal
    mostrarMenu()

main()