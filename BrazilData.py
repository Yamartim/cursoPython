from validate_docbr import CPF as vcpf, CNPJ as vcnpj
from re import findall
from datetime import datetime #, timedelta # nao usei mas n esquecer que tb é legal
import requests

class DocumentoFactory:

    @staticmethod
    def geradoc(doc):
        documento = str(doc)

        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError('não existe documento desse tamanho')

class Documento:

    @property
    def doc(self):
        return self._doc

    def __str__(self):
        #return f'{self._cpf[:3]}.{self._cpf[3:6]}.{self._cpf[6:9]}-{self._cpf[9:]}'
        return self._validador.mask(self.doc)


class DocCPF(Documento):
    def __init__(self, doc: str) -> None:
        self._validador = vcpf()
        if not self._validador.validate(doc):
            raise ValueError('CPF não exise')

        self._doc = doc

class DocCNPJ(Documento):
    def __init__(self, doc: str) -> None:
        self._validador = vcnpj()
        if not self._validador.validate(doc):
            raise ValueError('CNPJ não existe')

        self._doc = doc

def telefonebrmask(tel:str):
    "transforma o argumento em uma string formatada como um telefone brasileiro"
    tel = str(tel)

    pattern = r'(\d{2,3}?)(\d{2})(\d{4,5})(\d{4})'
    # a interrogação deixa o primeiro grupo lazy, enquanto o terceiro é greedy
    # assim captura os numeros melhor

    matches = findall(pattern, tel)[0]

    if not matches:
        raise ValueError('telefone invalido')

    #print(matches)
    if matches[0]:
        return f'+{matches[0]} ({matches[1]}) {matches[2]}-{matches[3]}'
    else:
        return f'({matches[1]}) {matches[2]}-{matches[3]}'
    

def databr(data:datetime = datetime.today()):
    "retorna uma string em formato brasileiro friendly"
    if type(data) != datetime:
        return ''

    diasemana = ['segunda feira', 'terça feira', 'quarta feira'
                'quinta feira', 'sexta feira', 'sabado', 'domingo']

    mes =  ['janeiro','fevereiro','março','abril',
            'maio','junho','julho','agosto',
            'setembro','outubro','novembro','dezembro']

    return data.strftime(f'{diasemana[data.weekday()]}, %d de {mes[data.month-1]} de %Y, %g:%m')

def req_api_cep(cep:str):
    cep = str(cep)
    if len(cep) != 8:
        return None
    
    url = f"https://viacep.com.br/ws/{cep}/json/"

    print(f'acessando cep {cep[:5]}-{cep[5:]}...')

    r = requests.get(url).json()

    return f"O endereço é: rua {r['logradouro']} do bairro {r['bairro']} na cidade {r['localidade']} do estado de {r['uf']}"