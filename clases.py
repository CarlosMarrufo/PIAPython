from datetime import datetime #Importamos datetime para agregar el momento automáticamente

class Participante: #Creación de la clase
    def __init__(self, correo, nombre, nacimiento, monto, folio = 0, momento = datetime.now()):
        self._correo = correo
        self._nombre = nombre
        self._nacimiento = nacimiento
        self._monto = monto
        self._folio = folio
        self._momento = momento.strftime("%Y-%m-%d %H:%M")
    
    def registrarParticipante(self): #Metodo para registrar la información del participante
        correo = self._correo
        nombre = self._nombre
        nacimiento = self._nacimiento
        monto = self._monto
        folio = self._folio
        momento = self._momento
        return(f'{correo} | {nombre.upper()} | {nacimiento} | {monto} | {folio} | {momento}')