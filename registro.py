def mostrarMenu(): #Función para mostrar el menú principal
    while(True):
        print(22*"#"+" MENÚ PRINCIPAL "+"#"*22)
        print("[1] Cargar información de CSV")
        print("[2] Registrar participantes")
        print("[3] Buscar participante")
        print("[4] Modificar participante")
        print("[5] Eliminar participante")
        print("[6] Ver lista de participantes")
        print("[7] Actualizar información de CSV")
        print("[8] Serializar información a JSON")
        print("[0] Salir")
        toDo = int(input('¿Qué opción deseas?: '))
        break
        
def main(): #Función principal
    mostrarMenu()

main()