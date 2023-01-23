from bytebank import Funcionario
import pytest

# tendo um diretorio chamado tests/ e um arquivo chamado test_<qulquercoisa>.py, é só rodar pytest no terminal q os metodos de teste sao realizados
# precisa do arquivo __init__.py tambem mesmo q esteja vazio

class TestClass:

    # quando o nome do metodo começa com 'test_' o pytest entende q é um teste a ser rodado
    # é bom escrever nomes detalhados pros testes (verbose) pra que seja facil de identificar no terminal qnd rodar o pytest
    def test_quando_idade_recebe_13_02_1998_retorna_25(self):
        # given... (dado esse contexto)
        entrada = '13/02/1998'
        esperado = 25

        funcionario_teste = Funcionario('teste', entrada, 1000)

        # when... (quando isso acontece)
        resultado = funcionario_teste.idade()

        # then... (o resultado é)
        assert resultado == esperado #assert é uma palavra chave do pytest

        # a metodologia given-when-then tambem tem uma alternativa chamada de arrange-act-assert 

    @pytest.mark.teste_nome
    def test_quando_nome_recebe_martim_lima_retorna_lima(self):
        entrada = 'Martim Lima'
        esperado = 'Lima'

        funcionario_teste = Funcionario(entrada, '10/10/2010', 1000)

        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado 

    @pytest.mark.teste_nome # marks sao "tags" pra rodar testes especificos
    def test_quando_decrescimo_salario_recebe_100000_retorna_90000(self):
        entrada_nome = "Martim Bilionario"
        entrada_salario = 100000
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '10/10/2010', entrada_salario)

        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado 

    @pytest.mark.skip
    def test_sus(self):
        assert True #esse teste n faz nadaaa

    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funconario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funconario_teste.calcular_bonus()

        assert resultado == esperado

    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception): # da pra testar se erros estao funcionando tb
            entrada = 100000000

            funconario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()

            assert resultado

'''
TDD - test driven development: criar PRIMEIRO o teste que o codigo tem que passar pra nós determinarmos se está bom, DEPOIS criar o código que vai ter que passar no teste, em seguida refatorar o código pra melhorar cada vez mais

fazendo testes primeiro faz com que os requisitos do projeto se tornem requerimentos que o código tem que cumprir desde o começo, aumentando a qualidade

decoradores pytest:
-v faz o relatorio ser verbose e mostrar mais detalhes
-k <string> faz apenas os tests filtrados pela string de busca
-m <mark> roda a mark especifica
--markers lista todos os marks padroes do pytest e o que eles fazem

--cov mostra o quanto de codigo esta sendo cobero pelos testes se pytest-cov esta instalado
--cov=<pastas> selecionas diretorios especificos pra analisar
--cov-report term-missing mostra quais linhas estão faltando ser cobertas 
--cov-report html da um relatorio bonitinho em forma de site 
--cov-report xml da um relatorio bonitinho em forma de xml 
'''