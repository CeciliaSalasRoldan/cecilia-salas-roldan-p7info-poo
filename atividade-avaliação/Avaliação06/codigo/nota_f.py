"""
    Modulo nota_fiscal
    Classe Nota_Fiscal
    Propriedades: - identidade - apresentado
                  - codigo - apresentado
                  - cliente - apresentado
                  - items - apresentado
                  - data - apresentado
                  - valornota_f - computado

"""
import datetime
from mainclient       import Cliente
from produto        import Produto
from notaf_item import NotaF_Item

from aplicação import datab


class NotaFiscal(datab.Model):
    __tablename__ = "TB_NOTA_FISCAL"
    identidade = datab.Column(datab.Integer, primary_key=True)
    codigo = datab.Column(datab.String)
    cliente = datab.Column(datab.String, datab.ForeignKey("TB_CLIENTE.codigo")) 
    data = datab.Column(datab.DateTime)
    valornota_f = datab.Column(datab.Float)

    cliente = datab.relationship('Cliente', foreign_keys=codigo)      

    def __init__(self, Identidade, codigo, cliente):
        self._Identidade = Identidade
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valornota_f=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
        
    def calcularNotaFiscal(self):
        valor=0.0
        itens=NotaF_Item.query.filter_by(id_notaf=self.identidade)
        for item in self._itens:
            valor = valor + item._valorItem
        self.valornota_f=valor
     
    def imprimirNotaFiscal(self):       
        pass