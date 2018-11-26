import pydoc

class Cita:

    """CLASE:
----------------------------------------------------------------------------
La clase Cita me permite guardar los datos relevantes de una cita medica:
nombre, apellido, edad, fecha, enfermedad y receta. Esta clase, ademas,
almacena los datos de tal forma que otras clases puedan interactuar con los
datos de las listas.
----------------------------------------------------------------------------
"""

    def __init__(self,nombre,apellido,edad,fecha,enfermedad,receta):
        '''METODO: __init__
Registra un paciente nuevo.
VARIABLES: self, nombre, apellido, edad, fecha, enfefrmedad y receta.
'''
        self.name = nombre
        self.last = apellido
        self.age = edad
        self.date = fecha
        self.sick = enfermedad
        self.receta = receta

    def All(self):
        '''METODO: All
Da la información general del paciente
VARIABLES: self
'''
        return ("El nombre del paciente es {0} {1}. Su edad {2}, su última visita fue el {3}. Tiene: {4}. Se le receto: {5}.".format(self.name,
                                                                                                                                          self.last,
                                                                                                                                          self.age,
                                                                                                                                          self.date,
                                                                                                                                          self.sick,
                                                                                                                                          self.receta))
    

    def getNombre(self):
        '''METODO: getNombre
returna solo el nombre del paciente.
VARIABLES: self
'''
        return "El nombre del paciente es: {}".format(self.name)

    def getApellido(self):
        '''METODO: getApellido.
returna solo los apellidos del paciente.
VARIABLES: self
'''
        return "Sus appelidos del paciente son: {}".format(self.last)

    def getEdad(self):
        '''METODO: getEdad
returna solo lac edad del paciente.
VARIABLES: self
'''
        return "La edad del paciente es: {}".format(self.age)

    def getFecha(self):
        '''METODO: getFecha
returna solo la fecha en el que el paciente tuvó su última cita.
VARIABLES: self
'''
        return "la última cita del paciente fue: {}".format(self.date)

    def getEnfermedad(self):
        '''METODO: getEnfermedad
returna lo que tiene el paciente.
VARIABLES: self
'''
        return "la última cita del paciente fue diagnosticado con: {}".format(self.sick)

    def getReceta(self):
        '''METODO: getRece
returna la última receta que llevó el paciente.
VARIABLES: self
'''
        return "Se le recetó: {}".format(self.receta)

    def setFecha(self, fecha):
        '''METODO: setFecha
Actualiza la fecha en el que paciente vinó por última vez.
VARIABLES: self y fecha(nueva fecha)
'''
        self.date = fecha

    def setReceta(self, receta):
        '''METODO: setReceta
Actualiza la receta que debe tomar el paciente.
VARIABLES: self y receta (nueva receta)
'''
        self.receta = receta

    def setEdad(self, edad):
        '''METODO: setEdad
Actualiza la edad del paciente.
VARIABLES: self y edad (nueva edad)
'''
        self.age = edad

    def setEnfermedad(self, enfermedad):
        '''METODO: setEnfermedad
Actualiza la enfermedad del paciente.
VARIABLES: self y enfermedad (si ha cambiado)
'''
        self.sick = enfermedad

    def saveDate(self):
        '''METODO: saveDate
Retorna la fecha.
VARIABLES: self
'''
        return self.date

    def saveReceta(self):
        '''METODO: saveReceta
Retorna la receta.
VARIABLES: self
'''
        return self.receta

    def saveEnfermedad(self):
        '''METODO: saveEnfermedad
Retorna la enfermedad.
VARIABLES: self
'''
        return self.sick

    def ls(self):
        '''METODO: ls
Retorna una lista con los datos de Cita para el paciente.
VARIABLES: self'''
        return [self.name,self.last,self.age,self.date,self.sick,self.receta]

#DOCUMERNTACION
print(Cita.__doc__)
print(Cita.__init__.__doc__)
print(Cita.All.__doc__)
print(Cita.getNombre.__doc__)
print(Cita.getApellido.__doc__)
print(Cita.getEdad.__doc__)
print(Cita.getFecha.__doc__)
print(Cita.getEnfermedad.__doc__)
print(Cita.getReceta.__doc__)
print(Cita.setFecha.__doc__)
print(Cita.setReceta.__doc__)
print(Cita.setEdad.__doc__)
print(Cita.setEnfermedad.__doc__)
print(Cita.saveDate.__doc__)
print(Cita.saveReceta.__doc__)
print(Cita.saveEnfermedad.__doc__)
print(Cita.ls.__doc__)
   
