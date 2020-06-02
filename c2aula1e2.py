def play():

	print("----------------------------------")
	print("the games of forca shall begin")
	print("-------------------------------gay")


	palavra = 'gambiarra'
	
	perdeu = False
	acertou = False
	
	#enquanto o jogador nao perder e nao acertar a palavra o jogo continua....
	while(not perdeu and not acertou): #todas as palavras chave em python são em letra minuscula, True e False são excessões pois são valores
		print("continuando game loop...")
		
		guess = input("manda a letra bonitao ")
		guess = guess.strip() #strip tira todos os espacos da string, vale a pena explorar metodos da classe string!
		
		index = 0
		for letra in palavra:
			if(guess.upper() == letra.upper()):	#upper retorna tudo em letra maiuscula
				print('encontrou a letra {} na posicao {}'.format(guess, index))
			index = index + 1
		

	print("GAME OVER")
	
if(__name__ == '__main__'):
	play()
