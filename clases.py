from datetime import datetime #Importamos datetime para agregar el momento automáticamente

class Participante: #Creación de la clase
    def __init__(self, correo, nombre, nacimiento, momento = datetime.now()):
        self._correo = correo
        self._nombre = nombre
        self._nacimiento = nacimiento
        self._momento = momento.strftime("%Y-%M-%D %H:%M")
    
    def mostrarInfo(self): #Metodo para mostrar la información del participante
        correo = self._correo
        nombre = self._nombre
        nacimiento = self._nacimiento
        momento = self._momento
        return(f'Correo: {correo}, Nombre: {nombre}, Nacimiento: {nacimiento}, Momento: {momento}')