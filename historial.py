import pydoc
import stack
import cita

class Historial:
    '''CLASE:
-----------------------------------------------------------------------------------
La clase Historial me permite almacenar los datos de cadaa cita por separado en
forma de lista.
-----------------------------------------------------------------------------------
'''

    def __init__(self, paciente):
        """METODO: __init__
Crea un Stack y agrega directamente la primera cita del paciente.
VARIABLES: self y paciente
"""
        self.historial = stack.Stack()
        self.historial.push(paciente.ls())

    def __str__(self):
        """METODO: __str__
Retorna el stack craeado en tipo string.
VARIABLES: self
"""
        return str(self.historial)

    def addCita(self,paciente):
        """METODO: addCita
Agrega un item al stack historial.
VARIABLES: self y paciente
"""
        self.historial.push(paciente.ls())
        inspect.getdoc(Cita)

#DOCUMENTACION
print(Historial.__doc__)
print(Historial.__init__.__doc__)
print(Historial.__str__.__doc__)
print(Historial.addCita.__doc__)



