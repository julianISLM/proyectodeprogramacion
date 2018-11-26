import  pydoc

class Stack:
    '''CLASE:
---------------------------------------------------------------------
La clase Stack me permite implementar la herramienta de stacks de
Python. Sin embargo, le añadimos el metodo Clear, pues, para nuestro
objetivo de proyecto, es necesario eliminar el stack de un paciente
cuando este muere.
---------------------------------------------------------------------

'''
def __init__(self):
        '''METODO: __init__
Crea un Stack vacío.
VARIABLES: self.
'''
        self.items = []

    def isEmpty(self):
        '''METODO: isEmpty
Hace un test para observar si el Stack está vacío.
VARIABLES: self
'''
        return self.items == []

    def push(self, item):
        '''METODO: Push
Agrega un item al Stack.
VARIABLES: self e item(item a agregar al stack)
'''
        self.items.append(item)

    def pop(self):
        '''METODO: pop
Returna el último item guardado en el Stack y lo remueve.
VARIABLES: self
'''
        return self.items.pop()

    def peek(self):
        """METODO: peek
Retorna el último item puesto en el stack.
VARIABLES: self
"""
        return self.items[len(self.items)-1]

    def size(self):
        """METODO: size
Retorna el numero de items en el stack.
VARIABLES: self
"""
        return len(self.items)

    def __str__(self):
        '''METODO: __str__
Retorna self.items de forma string.
VARIABLES: self
'''
        return str(self.items)

    def clear(self):
        '''METODO: clear
vacia el stack de todos sus elementos.
VARIABLES: self
'''
        while (self.isEmpty() == False):
            self.pop()

print(Stack.__doc__)
print(Stack.__init__.__doc__)
print(Stack.isEmpty.__doc__)
print(Stack.push.__doc__)
print(Stack.pop.__doc__)
print(Stack.peek.__doc__)
print(Stack.size.__doc__)
print(Stack.__str__.__doc__)
print(Stack.clear.__doc__)
