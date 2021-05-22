from datetime import datetime #Importamos datetime para agregar el momento automáticamente

class Participante: #Creación de la clase
    def __init__(self, correo, nombre, nacimiento, momento = datetime.now()):
        self.__correo = correo
        self.__nombre = nombre
        self.__nacimiento = nacimiento
        self.__momento = momento
    
    @classmethod
    def mostrarInfo(self): #Metodo para mostrar la información del participante
        correo = self.__correo
        nombre = self.__nombre
        nacimiento = self.__nacimiento
        momento = self.__momento
        return(f'Correo: {correo}, Nombre: {nombre}, Nacimiento: {nacimiento}, Momento: {momento}')