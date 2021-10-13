class Pilha:
    def __init__(self):
        self.elemento = list()

    def add_elemento(self, elemento_novo):
        self.elemento.append(elemento_novo)

    def tirar_elemento(self):
        del self.elemento[-1]

    def mostrar_pilha(self):
        print(*self.elemento)

pilha1 = Pilha()
pilha1.add_elemento(1)
pilha1.add_elemento(2)
pilha1.add_elemento(3)
pilha1.add_elemento(4)
pilha1.add_elemento(5)
pilha1.add_elemento(6)

print("Pilha:")
pilha1.mostrar_pilha()
print("Removendo elemento da pilha:")
pilha1.tirar_elemento()
pilha1.mostrar_pilha()
print("Pilha atualizada!")
