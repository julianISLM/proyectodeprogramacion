import stack
import cita

class Historial:

    def __init__(self, paciente):
        """Crea un Stack y agrega directamente la primera cita del paciente"""
        self.historial = stack.Stack()
        self.historial.push(paciente.ls())

    def __str__(self):
        """Retorna el stack craeado en tipo string"""
        return str(self.historial)

    def addCita(self,paciente):
        """Agrega un item al stack historial"""
        self.historial.push(paciente.ls())
        


