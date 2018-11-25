class Historial(cita, stack):
    def __init__(self):
        self.historial = []

    def AddCita(self):
        self.historial.push(Cita.All(DatosDeLaCita))
        return self.historial
