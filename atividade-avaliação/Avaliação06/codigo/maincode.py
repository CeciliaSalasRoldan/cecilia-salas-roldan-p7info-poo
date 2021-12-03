"""
  Módulo maincode - Ele vai instanciar os objetos apresentados no conjunto do módulo 01  
"""
from produto        import Produto
from mainclient        import Cliente
from nota_f     import NotaFiscal
from notaf_item import NotaF_Item
from tipo_cl    import Tipo_Cliente

def main():
    
    clnt=Cliente(1, "Carlos André", 100, "880.289.850.25", 1)
    
    prdt1=Produto(1,100,"Goiabada", 5.5) 
    item1=NotaF_Item(1, 1, 10, prdt1)
    
    prdt2=Produto(2,200,"Vinagre de Maça", 8.5) 
    item2=NotaF_Item(2, 2, 10, prdt2)
    
    prdt3=Produto(3,300,"Feijão de Corda", 4.5) 
    item3=NotaF_Item(3, 3, 10, prdt3)
    
    nota_f = NotaFiscal(1,100,clnt)
    
    nota_f.addItem(item1)
    
    nota_f.addItem(item2)
    
    nota_f.addItem(item3)
    
    nota_f.calcNotaFiscal()
    
    print("Valor Nota Fiscal= " + str(nota_f.valorNota))
    
    nota_f.imprimirNotaFiscal()


if __name__ == '__main__':
    main()