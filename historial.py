class Historial:
    def __init__(self, paciente, historial = stack.Stack()):
        self.historial = historial
        historial.push(paciente.ls())

    def __str__(self):
        return str(self.historial)
