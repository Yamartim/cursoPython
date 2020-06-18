import random

def play():
    
    desenhar_abertura()
    
    palavra = load_palavra()
    acertos = ['_' for letra in palavra]    #recurso list comprehention

    gamestate_final = iniciar_gameloop(palavra, acertos)

    ganhou = gamestate_final[0]
    perdeu = gamestate_final[1]

    terminar_jogo(ganhou, perdeu)



def desenhar_abertura():
    
    print("----------------------------------")
    print("the games of forca shall begin")
    print("-------------------------------gay")

def load_palavra(nome_arquivo = "c2palavras.txt"):  #essa atribuicao serve pra setar um parametro facultativo com valor default
    
    # palavra = 'gambiarra'.upper()
    # acertos = ['_', '_', '_', '_', '_', '_', '_', '_', '_'] #tipo 'list' do python, diferente de array
    
    # acertos = []
    # for letra in acertos:
    #     acertos.append('_')
    #funciona, mas python permite um jeito mais interessante...
    
    # arquivo = open("c2palavras.txt", "r")
    # lista_palavras = []
    # for linha in arquivo:
    #     linha = linha.strip()
    #     lista_palavras.append(linha)
    
    # arquivo.close()
    
    lista_palavras = []
        
    with open(nome_arquivo) as arquivo:   #sintaxe especial do python pra lidar com arquivos de forma mais segura
        for linha in arquivo:
            linha = linha.strip()
            lista_palavras.append(linha)
    
    indice_pal = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[indice_pal].upper()
    
    return palavra_secreta
 
def iniciar_gameloop(pal, acert):
    gan = False
    per = False
    erros = 0

    desenhar_forca(0)
    print(acert)

	#enquanto o jogador nao perder e nao acertar a palavra o jogo continua....
	# while(not perdeu and not acertou): #todas as palavras chave em python são em letra minuscula, True e False são excessões pois são valores
    while(not (per or gan)):          #demorgan gang lmao
        print("continuando game loop...")

        guess = parse_chute()
        
        if(guess in pal):
            validar_tentativa(acert, pal, guess)
        else:
            erros+=1


        desenhar_forca(erros)
        print(acert)

        per = erros >= 6
        gan = '_' not in acert
    
    return [gan, per]

def desenhar_forca(n):
    
    variation = random.randrange(0, 4)
    
    print('                 ')
    print('    __________   ')
    print('    |/       |   ')
    
    if(n > 0):
        print('    |        O   ')
        if(n == 2):
            print('    |        |   ')
        elif(n == 3):
            if((variation == 1) or (variation == 2)):
                print('    |       -|   ')
            else:
                print('    |        |-  ')
        elif(n >= 4):
            print('    |       -|-  ')
        else:
            print('    |            ')
            
        if(n == 5):
            if((variation == 1) or (variation == 3)):
                print('    |       /    ')
            else:
                print('    |        \    ')
        elif(n >= 6):
            print('    |       /\   ')
        else:
            print('    |            ')
            
    else:
        for i in range(0, 3):
            print('    |            ')
        
    print('    |            ')
    print('  __|__          ')
    print('  |-|-|          ')
    print('                 ')
    
def parse_chute():
    chute = input("manda a letra bonitao ")
    chute = chute.strip().upper()       #strip tira todos os espacos da string, vale a pena explorar metodos da classe string!
    return chute[0]
    
def validar_tentativa(alvo, string, char):
    index = 0
    for letra in string:           #letra varre todos os elementos em palavra
        if(char == letra):         #upper retorna tudo em letra maiuscula
            alvo[index] = letra
        index += 1

def terminar_jogo(gan, per):
    print("GAME OVER")
    print()

    if(per):
        print('OMAE WA MOU SHINDEIRU')
    elif(gan):
        print('parabains shinji')
    else:
        print('wtf voce quebrou meu codigo porra!')


if(__name__ == '__main__'):
	play()


