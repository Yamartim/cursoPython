from abc import ABCMeta, abstractmethod
from functools import total_ordering

# herdar ABCMeta como metaclass faz metodos abstratos funcionarem
# fazer isso transforma a classe em abstrata, nao pode instanciar ela por si só tem que instanciar por uma filha

#o decorador total_ordering faz com que tendo implementado só uma função de igualdade e uma de ordenação entre dois objetos (__eq__ e __lt__ nesse caso) todas as outras comparações como <=, >, !=, >=... sejam lógicamente determinadas, muito brabo

@total_ordering
class Programa(metaclass=ABCMeta): 
    def __init__(self, nome:str, ano:int) -> None:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0 
        # self.__<atributo> => private, 
        # self_<atributo> => protected, ideal pra herança

    # getters e setters
    # jeito feio de acessar um atributo privado de fora da classe em python é com a função attrgettr(<nome do atributo>) (attrgettr é da biblioteca operator)
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

    # mais um dunder brabo: __lt__ de "lesser than" pra fazer comparações > e <
    # bem util pra dar sort em listas de objetos
    # nao exte um "greater than" pq seria so oposto do lt big brain
    # isso chama "ordenação natural de objetos"
    def __lt__(self, __o: object) -> bool:
        if isinstance(__o, Programa):
            if self._likes != __o._likes:
                return self._likes < __o._likes 
            elif self.ano != __o.ano:
                return self.ano < __o.ano
            else:
                return self._nome < __o._nome
            # assim ficam ordenados em likes, e se o numero de likes for igual, compara ano de lançamento, se for o mesmo, ordem alfabetica
        else:
            return False

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Programa):
            return self._nome != __o._nome
        return False

    @abstractmethod
    def abstratinho(self):
        pass


    
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

    def abstratinho(self):
        print('yooo estou implementado no filma')

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

    # implementação do metodo abstrato é forçado pelo ABCMeta, se nao fizer da erro
    def abstratinho(self):
        print('yooo estou implementado no no anime')



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
    #nome disso é duck typing: 
    #   "não importa se é um pato e sim se se comporta como pato"
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

class ListaMutavel(MutableSequence):
    pass

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

totoro.abstratinho()
mobpsycho.abstratinho()