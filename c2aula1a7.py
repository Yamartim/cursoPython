import random

def play():
    
    print("----------------------------------")
    print("the games of forca shall begin")
    print("-------------------------------gay")
    
    
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
        
    with open("palavras.txt") as arquivo:   #sintaxe especial do python pra lidar com arquivos de forma mais segura
        for linha in arquivo:
            linha = linha.strip()
            lista_palavras.append(linha)
    
    
    indice_pal = random.randrange(0, len(lista_palavras))
    palavra = lista_palavras[indice_pal].upper()
    acertos = ['_' for letra in palavra]    #recurso list comprehention
    
    perdeu = False
    ganhou = False
    erros = 0
	
    desenhar_forca(0)
    print(acertos)
	
	#enquanto o jogador nao perder e nao acertar a palavra o jogo continua....
	# while(not perdeu and not acertou): #todas as palavras chave em python são em letra minuscula, True e False são excessões pois são valores
    while(not (perdeu or ganhou)):          #demorgan gang lmao
        print("continuando game loop...")
		
        guess = input("manda a letra bonitao ")
        guess = guess.strip().upper()       #strip tira todos os espacos da string, vale a pena explorar metodos da classe string!
		
        if(guess in palavra):
            index = 0
            for letra in palavra:           #letra varre todos os elementos em palavra
                if(guess == letra):         #upper retorna tudo em letra maiuscula
                    acertos[index] = letra
                index += 1
        else:
            
            erros+=1
    		
		
        desenhar_forca(erros)
        print(acertos)
		
        perdeu = erros >= 6
        ganhou = '_' not in acertos 

    print("GAME OVER")
    print()
	
    if(perdeu):
	    print('OMAE WA MOU SHINDEIRU')
    elif(ganhou):
	    print('parabains shinji')
    else:
	    print('wtf voce quebrou meu codigo porra!')
	    
	    
	
def desenhar_forca(n):
    
    variation = random.randrange(0, 4)
    
    print('                 ')
    print('    __________   ')
    print('    |        |   ')
    
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
	
	
if(__name__ == '__main__'):
	play()


