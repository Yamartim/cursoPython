
class Programa:
    def __init__(self, nome:str, ano:int) -> None:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0 
        # self.__<atributo> => private, 
        # self_<atributo> => protected, ideal pra herança

    #getters e setters
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome:str):
        self._nome = nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    #metodo "tostring()" reservado do python
    def __str__(self) -> str:
        return f'{self._nome} de {self.ano} tem {self._likes} likes'

    #da pra usar __repr__ tambem, de representação
    #metodos com __ antes e depois se chamam magic ou dunder methods (Double UNDERscore)
    
#herdando de programa, super() representa a classe mae
class Filme(Programa):
    def __init__(self, nome: str, ano: int, duracao:int) -> None:
        super().__init__(nome, ano)
        self.duracao = duracao

    # decorador pra dar metodos q nao precisam da classe instanciada pra serem chamados, cls é convençao assim como self
    @classmethod 
    def initial_likes(cls):
        return f'o numero inicial de likes de um filme é {cls.likes}'

    def __str__(self) -> str:
        return f'{self._nome} de {self.ano} dura {self.duracao} minutos e tem {self._likes} likes'

class Anime(Programa):
    def __init__(self, nome: str, ano: int, temporadas:int) -> None:
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # decorador pra declarar metodo estatico duh
    @staticmethod
    def weebness():
        return 'o nivel de weebness atual é ridiculo'
    
    def __str__(self) -> str:
        return f'{self._nome} de {self.ano} com {self.temporadas} temporadas tem {self._likes} likes'


totoro = Filme('tonari no totoro', 1999, 100)
totoro.dar_like()
totoro.dar_like()
totoro.dar_like()

mobpsycho = Anime('mob psycho 100', 2016, 3)
mobpsycho.dar_like()
mobpsycho.dar_like()

#polimorfismo

#lista = [totoro, mobpsycho]
#for programa in lista:
    #print(programa)

#herdando da classe list pra fazer um objeto iteravel
# é uma gambiarra, list tem mtos metods q nao tem como a gente saber o q fazer
""" 
class Playlist(list):
    def __init__(self, nome, lista) -> None:
        super().__init__(lista)
        self.nome = nome 
"""
#versao big brain
class Playlist():
    def __init__(self, nome, lista) -> None:
        self.nome = nome
        self.__lista = lista #composição ao contrario de herança nao aumenta acoplamento

    @property
    def lista(self):
        return self.__lista

    #só definir isso aqui ja transforma o obj em iteravel com indice, in...
    #nome disso é duck typing
    def __getitem__(self, item): 
        return self.__lista[item]
    
    def __len__(self):
        return len(self.__lista)


inside = Filme('inside', 2021, 120)
inside.dar_like()
inside.dar_like()
inside.dar_like()
inside.dar_like()

hxh = Anime('hunter x hunter', 2011, 6)
hxh.dar_like()
hxh.dar_like()
hxh.dar_like()
hxh.dar_like()
hxh.dar_like()
hxh.dar_like()

lista = [totoro, mobpsycho, inside, hxh]
pl = Playlist('minha playlist', lista)

for pgr in pl:
    print(pgr)

print(mobpsycho in pl)
print(len(pl))

'''
PYTHON DATA MODEL
    metodo de inicialização: __init__
    metodos de representação: __str__, __repr__
    metodos de container, sequencia: __contains__, __iter__, __len__, __getitem__
    metodos numericos (sobrecarga operadores): __add__, __sub__, __mul__, __mod__
'''

'''
Classes abstratas

from abc import ABC 
from collections.abc import MutableSequence

    abc = abstract base classes
    da pra fazer classe abstrata na mao no python mas é gambiarra, melhor importar dessa biblioteca
    os metodos das ABCs nao sao completamente abstratos, da pra implementar com super() se nao quiser criar do zero

criando uma classe abstrata:

from abc import ABCMeta, abstractmethod 

class Programa(metaclass = ABCMeta): 
    @abstractmethod 
    def __str__(self): 
        pass

assim o metodo __str__ precisa ser obrigatoriamente implementado
'''