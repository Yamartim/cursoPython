from URLParser import URLParser
import re

'''
# coisas de string pra lembrar

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
print(url)

# tratamento de excessoes: isso causa um traceback que printa a mensagem
if url == '':
    raise ValueError('A URL está vazia!')

# pra separar a base dos parametros da pra usar o metodo find
indice = url.find('?') #retorna o indice da interrogalçao

# no fatiamento de string/lista, o numero da esquerda é inclusivo e o da direita é exclusivo
url_base = url[0:indice] 

# deixar um campo vazio retorna td ate o começo/final
url_param = url[indice+1:]

print(url_base, url_param)

# retorna a posição do 'm' onde a string de busca começa
parametro = 'quantidade'
#parametro = 'moedaOrigem'
#parametro = 'moedaDestino'
param_indice = url_param.find(parametro) 

# o segundo arg de find é a posiçao inicial, se nao achar nenhum caractere retorna -1
indice_e = url_param.find('&', param_indice) 

if indice_e != -1:
    param_valor = url_param[param_indice+len(parametro)+1:indice_e]

else:
    #indice do valor = indice do parametro + tamanho do parametro + 1 (representa o '=')
    param_valor = url_param[param_indice+len(parametro)+1:]

print(param_valor)
 
#'''

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
parser = URLParser(url)
""" 
print(parser.url)
print(parser.url_base)
print(parser.url_param)

print(parser.value('quantidade'))
print(parser.value('moedaOrigem'))
print(parser.value('moedaDestino'))
 """

#regex = re.compile('(http(s)?://)?(www.)?\w+.com(.br)?').search(url).group()
#regex = re.findall(r'\w+=', url)

#print(parser.keys())
#print(parser.values())

print(parser)

VALOR_REAL = 1.00
VALOR_DOLAR = 5.50
VALOR_EURO = 999.00

def valormoeda(moeda):
    if moeda == 'real':
        return VALOR_REAL
    elif moeda == 'dolar':
        return VALOR_DOLAR
    elif moeda == 'euro':
        return VALOR_EURO

qtd = float(parser.value('quantidade'))
org = valormoeda(parser.value('moedaOrigem'))
dst = valormoeda(parser.value('moedaDestino'))

conversao =  qtd * org / dst 

print('o valor da conversao é', conversao)

# se nao sobrecarregar o metodo __equals__ o python compara os endereços de memoria
# o operador 'is' compara endereços de memoria, por isso funciona com None
# da pra ver o endereço de memoria de qualquer objeto pela funcao id()

#parser2 = URLParser(url)
#print(parser == parser2)
#print(parser == 'oi')

'''
 no python coisas "vazias" sao cosideradas num if como falso como None, 0, string vazia...
 por outro lado coisas com conteudo como numeros != 0 e strings nao vazias sao true

 da pra usar a função bool() em uma variavel pra ver se ela é false ou true

 por algum motivo o float 0.0 é true tho lmao
'''
