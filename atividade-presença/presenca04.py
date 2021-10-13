class Fila:
    def __init__(self):
        self.elemento = list()

    def add_elemento(self, elemento_novo):
        self.elemento.append(elemento_novo)

    def tirar_primeiro_elemento(self):
        del self.elemento[0]

    def mostrar_fila(self):
        print(*self.elemento)

fila1 = Fila()
fila1.add_elemento(1)
fila1.add_elemento(2)
fila1.add_elemento(3)
fila1.add_elemento(4)
fila1.add_elemento(5)
fila1.add_elemento(6)

print("Fila (First in First out):")
fila1.mostrar_fila()
print("Removendo o primeiro elemento da fila:")
fila1.tirar_primeiro_elemento()
fila1.mostrar_fila()
print("Fila atualizada!")
