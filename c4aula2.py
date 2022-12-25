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
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        self._nome = nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1
    
#herdando de programa, super() representa a classe mae
class Filme(Programa):
    def __init__(self, nome: str, ano: int, duracao:int) -> None:
        super().__init__(nome, ano)
        self.duracao = duracao

    # decorador pra dar metodos q nao precisam da classe instanciada pra serem chamados, cls é convençao assim como self
    @classmethod 
    def initial_likes(cls):
        return f'o numero inicial de likes de um filme é {cls.likes}'

class Anime(Programa):
    def __init__(self, nome: str, ano: int, temporadas:int) -> None:
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # decorador pra declarar metodo estatico duh
    @staticmethod
    def weebness():
        return 'o nivel de weebness atual é ridiculo'
