"""
    Modulo notaf_item
    Classe NotaF_Item
    Propriedades: _identidade - computado  
                  _qtd - computado  
                  _sequencial - computado  
                  _valor - computado  
                  _produto - computado  
""" 
#imports-------------------------------
from produto import Produto
from aplicação import datab

#Class----------------------------------
class NotaF_Item(datab.Model):
    __tablename__ = "TB_ITEM_NF"
    identidade = datab.Column(datab.Integer, primary_key=True)
    id_notaf = datab.Column(datab.Integer, datab.ForeignKey("TB_NOTA_FISCAL.identidade")) 

    sequencial = datab.Column(datab.String)
    qtd = datab.Column(datab.Integer)

    produto = datab.Column(datab.String, datab.ForeignKey("TB_PRODUTO.produto")) 
    descricao = datab.Column(datab.String, datab.ForeignKey("TB_PRODUTO.descricao")) 

    valorUnidade = datab.Column(datab.Float, datab.ForeignKey("TB_PRODUTO.valorUnidade")) 
    valorItem = datab.Column(datab.Float)
#---------------------------------------------------------------------------------------------
    nota_fiscal = datab.relationship('NotaFiscal', foreign_keys=id_notaf)
    produto = datab.relationship('Produto', foreign_keys=produto)

    descricao = datab.relationship('Produto', foreign_keys=descricao) 
    valor_unidade = datab.relationship('Produto', foreign_keys=valorUnidade) 
#---------------------------------------------------------------------------------------------
    def __init__(self, identidade, sequencial, qtd, produto):
        self._identidade=identidade
        self._sequencial=sequencial
        self._qtd=qtd
        self._produto=produto
        self._descricao=self._produto.getDescricao()
        self._valorUnidade=self._produto.getValorUnidade()
        self._valorItem=float(self._qtd * self._valorUnidade)
      
    def str(self):
        string="\nIdentidade={5} Sequencial={4} Qtd={3} Produto={2} Valor Unidade={1} Valor Item={0}".format(self._valorItem,
                                                                                                             self._valorUnidade,
                                                                                                             self._descricao, 
                                                                                                             self._qtd, 
                                                                                                             self._sequencial, 
                                                                                                             self._identidade)
        return string

#--------------------------------------------------------------------------------------------   
if __name__ == '__main__':
    produto = Produto(1,100,'Farinha Amarela', 5.5) 

    item=NotaF_Item(1, 1, 12, produto)
    print(item.str())