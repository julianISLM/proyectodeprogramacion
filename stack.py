class Stack:

    def __init__(self):
        '''Crea un Stack vacío'''
        self.items = []

    def isEmpty(self):
        '''Hcae un test para observar si el Stack está vacío'''
        return self.items == []

    def push(self, item):
        '''Agrega un item al Stack'''
        self.items.append(item)

    def pop(self):
        '''Returna el último item guardado en el Stack y lo remueve'''
        return self.items.pop()

    def peek(self):

        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
