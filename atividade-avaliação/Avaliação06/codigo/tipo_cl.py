""" 
    Modulo tipo_cliente -
    Classe Tipo_Cliente - Lista os tipos de cliente
"""

import enum
class Tipo_Cliente(enum.Enum):
    pessoaFisica = 1
    pessoaJuridica = 2
     
if __name__ == '__main__':
    print ("Os numeros enum sao: ")
    for tipo_c in (Tipo_Cliente):
        print(type(tipo_c))
        print(tipo_c) 