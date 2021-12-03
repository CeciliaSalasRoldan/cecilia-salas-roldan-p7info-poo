"""
    Módulo produto
    Classe Produto
     Propriedades: _identidade -apresentado   
                  _codigo - apresentado  
                  _descrição - apresentado   
                  _valorUnnidade - apresentado 
"""
from aplicação import datab


class Produto(datab.Model):
    __tablename__ = "TB_PRODUTO"
    identidade = datab.Column(datab.Integer, primary_key=True)
    codigo = datab.Column(datab.String, unique=True)
    descricao = datab.Column(datab.String)
    valorUnidade = datab.Column(datab.Float)

    def __init__(self, identidade, codigo, descricao, valorUnidade):
        self._identidade = identidade
        self._codigo=codigo
        self._descricao=descricao
        self._valorUnidade=valorUnidade
        
    def getDescricao(self):
        return self._descricao
    
    def getValorUnitario(self): 
        return self._valorUnidade
        
    def str(self):
        string="\nIdentidade={3} Codigo={2} Descricao={1} Valor Unitario={0}".format(self._valorUnidade, self._descricao, self._codigo, self._identidade)
        return string
    
   
    
if __name__ == '__main__':
    produto=Produto(1,100,'Farinha Amarela', 5.5)        
    print(produto.str())