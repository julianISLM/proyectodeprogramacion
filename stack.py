class Stack:
    
    '''Contiene todos los metodos necesarios de esta herramienta. Sin embargo, se creo
    otro metodo adicional, "clear", el cual, elimina toda la informacion contenida en un stack.'''
    
    def __init__(self):
        '''Crea un Stack vacío'''
        self.items = []

    def isEmpty(self):
        '''Hace un test para observar si el Stack está vacío'''
        return self.items == []

    def push(self, item):
        '''Agrega un item al Stack'''
        self.items.append(item)

    def pop(self):
        '''Returna el último item guardado en el Stack y lo remueve'''
        return self.items.pop()

    def peek(self):
        """Retorna el último item puesto en el stack"""
        return self.items[len(self.items)-1]

    def size(self):
        """Retorna el numero de items en el stack"""
        return len(self.items)

    def __str__(self):
        '''Retorna toda la informacion del Stack en forma de string'''
        return str(self.items)

    def clear(self):
        '''Elimina automaticamente, todos los datos del stack'''
        while (self.isEmpty() == False):
            self.pop()
