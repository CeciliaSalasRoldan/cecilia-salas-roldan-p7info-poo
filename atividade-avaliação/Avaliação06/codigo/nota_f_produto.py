
from nota_f import NotaFiscal
from produto    import Produto

class NotaF_Produto():
    
    def __init__(self): 
        self._notas_Fiscais=[]
        self._produtos=[]
        
    def addNota_Produto(self, nota, produto):
        if isinstance (nota, NotaFiscal) and isinstance(produto,Produto): 
            self._notas_Fiscais.append(nota)
            self._produtos.append(produto)