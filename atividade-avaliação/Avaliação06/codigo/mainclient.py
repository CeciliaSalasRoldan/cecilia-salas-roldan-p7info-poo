"""
    Modulo cliente
    Classe Cliente
    Propriedades: _identidade - chave primaria - apresentado
                  _nome - nome cliente - apresentado
                  _tipo - tipo cliente - apresentado
                  _codigo - codigo cliente - apresentado
                  _cpfcnpj - cpf OU cnpj do cliente - apresentado  
"""
#Imports ----------------------------------------------------------
from tipo_cl  import Tipo_Cliente
from aplicação import datab

#Class ------------------------------------------------------------
class Cliente(datab.Model):
    __tablename__ = "TB_CLIENTE"
    identidade = datab.Column(datab.Integer, primary_key=True)
    nome = datab.Column(datab.String)
    codigo = datab.Column(datab.String, unique=True)
    cpfcnpj = datab.Column(datab.String, unique=True)

    def __init__(self, identidade, nome, codigo, cpfcnpj, tipo):
        self._identidade = identidade
        self._nome = nome
        self._codigo = codigo
        self._cpfcnpj = cpfcnpj
        self._tipo = tipo
        
    def str(self):
        string="\nIDENTIDADE={4} CODIGO={2} NOME={3} CPF/CNPJ={1} TIPO={0}".format(self._tipo, self._cpfcnpj, self._codigo, self._nome, self._identidade)
        return string
    
if __name__ == '__main__':
    cliente=Cliente(1, "Carlos Andre", 100, '880.289.850.25', Tipo_Cliente.PESSOA_FISICA)
    print(cliente.str())