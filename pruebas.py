import stack
import cita

pac = cita.Cita("Julian Orlando", "Medina Martìnez", "22", "16/11/2018", "Gripa", "Acetaminofen")

date = stack.Stack()
receta = stack.Stack()

def stack_date(x):
    '''Agrega al Stack 'date' del paciente x las diferentes fechas en las que vino'''
    date.push(x.saveDate())
    return str(date)
    
def stack_receta(x):
    '''Agrega al Stack 'receta' las recetas del paciente x'''
    receta.push(x.saveReceta())
    return str(receta)


##PRUEBAS DEL PRIMER PACIENTE
## el primer día que vinó.
stack_date(pac)
stack_receta(pac)



##  segunda cita que vino el mismo paciente

pac.setFecha("18/11/2018")
pac.setReceta("nada, porque se mejoró de la gripa.")
stack_date(pac)
stack_receta(pac) 


##tercera cita 
##el doctor quiere observar que fue lo último que se le receto al paciente y en que fecha

##aquí observa la cita anterior
date.pop()
receta.pop()

##Aquí observa la penultima cita
date.pop()
receta.pop()


pac.setFecha("24/12/2018")
pac.setReceta("Resulta que no era una gripa, era chikungunya. Se debe hospitalizar.")
stack_date(pac)
stack_receta(pac)
