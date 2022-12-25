# Herança multipla

class ClasseMaezona():
    def __init__(self, texto = 'um texto ai') -> None:
        self.texto = texto

    def letra_fav(self):
        print('-')

    def numero_fav(self):
        print(0)

class FilhaA(ClasseMaezona):
#    def letra_fav(self):
#        print('A')

    def numero_fav(self):
        print(10)


class FilhaB(ClasseMaezona):
    def letra_fav(self):
        print('B')

    def numero_fav(self):
        print(20)

class primo():
    def __str__(self):
        return f'esse é o texto da outra classe: {self.texto}'

class Neta1(FilhaA):
    pass

class Neta2(FilhaA, FilhaB):
    pass

class Neta3(FilhaA, FilhaB, primo):
    pass

obj_a = Neta1()

obj_a.letra_fav() # -
obj_a.numero_fav() # 10

obj_b = Neta2()

obj_b.letra_fav() # B
obj_b.numero_fav() # 10

obj_c = Neta3('texto da primeira classe kkkk')

obj_c.letra_fav() # B
obj_c.numero_fav() # 10

# pra decidir qual metodo rodar o python vai nessa ordem:
#   obj atual -> primeira classe mae -> classe mae da mae (ate nao ter mais) -> segunda classe mae
# o nome disso é MRO method resolution object

print(obj_a) # printa o endereço da memoria
print(obj_c) # printa a string q foi definida na Primo com o atributo da Mae
# da pra usar classes simples como a Primo pra "decorar" outras classes com pequenas funcionalidades especificas
# o nome disso é MIXIN
# como é feito só pra decorar e depende de outros objetos, n é pra instanciar um obj dela
