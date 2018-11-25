import stack
import cita

pac = cita.Cita("Julian Orlando", "Medina Martìnez", "22", "16/11/2018",
                "Gripa", "Acetaminofen")

date = stack.Stack()
receta = stack.Stack()
sick = stack.Stack()


def stack_date(x):
    '''Agrega al Stack 'date' del paciente las diferentes fechas en las que vino'''
    date.push(x.saveDate())

    return str(date)

def stack_sick(x):
    """agrega al stack 'sick' las enfermedades que ha tenido el paciente."""
    sick.push(x.saveEnfermedad())
    return str(sick)

    
def stack_receta(x):
    '''Agrega al Stack 'receta' las recetas del paciente'''
    receta.push(x.saveReceta())
    return str(receta)


##PRUEBAS DEL PRIMER PACIENTE
## el primer día que vinó.
stack_date(pac)
stack_receta(pac)
stack_sick(pac)



##  segunda cita que vino el mismo paciente
date.peek()
sick.peek()
receta.peek()

pac.setFecha("18/11/2018")
pac.setReceta("nada, porque se mejoró de la gripa.")
pac.setEnfermedad("nada")
stack_date(pac)
stack_receta(pac)
stack_sick(pac)




##tercera cita 
##el doctor quiere observar que fue lo último que se le receto al paciente y en que fecha

##aquí observa la cita anterior
date.peek()
receta.peek()
sick.peek()

##Aquí observa la primera cita cita
str(sick)
str(date)
str(receta)

pac.setFecha("24/12/2018")
pac.setEnfermedad("Puede ser chikungunya, por el dolor en articulaciones")
pac.setReceta("Se debe hospitalizar")
stack_date(pac)
stack_receta(pac)
stack_sick(pac)
