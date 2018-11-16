class Cita:

    def __init__(self,nombre,apellido,edad,fecha,enfermedad,receta):
        '''Registra un paciente nuevo'''
        self.name = nombre
        self.last = apellido
        self.age = edad
        self.date = fecha
        self.sick = enfermedad
        self.receta = receta

    def All(self):
        '''Da la información general del paciente'''
        return ("El nombre del paciente es {0} {1}. Su edad {2}, su última visita fue el {3}. Tiene: {4}. Se le receto: {5}".format(self.name,
                                                                                                                                          self.last,
                                                                                                                                          self.age,
                                                                                                                                          self.date,
                                                                                                                                          self.sick,
                                                                                                                                          self.receta))
    

    def getNombre(self):
        '''returna solo el nombre del paciente'''
        return "El nombre del paciente es: {}".format(self.name)

    def getApellido(self):
        '''returna solo los apellidos del paciente'''
        return "Sus appelidos del paciente son: {}".format(self.last)

    def getEdad(self):
        '''returna solo lac edad del paciente'''
        return "La edad del paciente es: {}".format(self.age)

    def getFecha(self):
        '''returna solo la fecha en el que el paciente tuvó su última cita'''
        return "la última cita del paciente fue: {}".format(self.date)

    def getEnfermedad(self):
        '''returna lo que tiene el paciente'''
        return "la última cita del paciente fue: {}".format(self.sick)

    def getReceta(self):
        '''returna la última receta que llevó el paciente'''
        return "Se le receto: {}".format(self.receta)

    def setFecha(self, fecha):
        '''Actualiza la fecha en el que paciente vinó por última vez'''
        self.date = fecha

    def setReceta(self, receta):
        '''Actualiza la receta que debe tomar el paciente'''
        self.receta = receta

    def setEdad(self, edad):
        '''Actualiza la edad del paciente'''
        self.age = edad

    def setEnfermedad(self, enfermedad):
        '''Actualiza la enfermedad del paciente'''
        self.sick = enfermedad

    
    

####PRUEBA
m = Cita("Julian", "Medina", "13", "18/06/2000", "Gripita", "Dolex forte")
m.setFecha("16/11/2018")
m.setReceta("vape")

