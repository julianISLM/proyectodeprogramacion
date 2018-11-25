import stack
import cita
import historial

###El mismo doctor recibe estos dos pacientes cada uno con sus
###repectivas caracteristicas
pac1 = cita.Cita("Julian Orlando", "Medina Martìnez", "22", "16/11/2018",
                "Gripa", "Acetaminofen")

pac2 = cita.Cita("Leonardo", "Leiva", "18", "24/11/2018",
                "Varicela", "cremas")

###crea un historial para cada paciente

histpac1 = historial.Historial(pac1)
histpac2 = historial.Historial(pac2)

###El paciente uno viene porque se mejoro
###el doctor decide modificar el historial del paciente 1
pac1.setFecha("25/11/2018")
pac1.setReceta("Nada, porque se mejoro")
pac1.setEnfermedad("Nada")
pac1.setEdad("23") ##porque hoy estaba de cumpleaños
histpac1.addCita(pac1)

str(histpac1) ##Revisa la informacion del paciente 1.

###Ese mismo doctor tiene otro paciente 2 el cual tambien debe modificar
pac2.setFecha("25/11/2018")
pac2.setReceta("Más Cremas")
pac2.setEnfermedad("Porque se le infecto una herida por tanto rascarse")
histpac2.addCita(pac2)

str(histpac2) ##Revisa la informacion del paciente 2.




