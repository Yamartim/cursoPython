import random						#importando a biblioteca (modulo), equivalente ao define ou include no c 

vidas = 0
pontos = 1000

print("~~~~~~~~~~~~")
print("Adivinhation games")
print("~~~~~~~~~~~~")


print("selecione o nivel de dificuldade")
print("1 - facil, 2 - médio, 3 - dificil ")

nivel = int(input("nivel: "))

if(nivel == 1):
	vidas = 20
elif(nivel == 2):
	vidas = 10
else:
	vidas = 5
	




num_secreto = random.randrange(1, 101)  #gera numero de 1 a 100
#random da um valor float de 0 a 1, entao multiplicamos por 100 e arredondamos
# num_secreto = round((random.random() * 100) + 1) #versao gambiarra
#vidas = 3
#nvidas = 0

#print(num_secreto) #debug

#while (vidas > nvidas):
for nvidas in range(0, vidas):

	#print("tens", vidas-nvidas, "de", vidas, "chances" )
	print("tens {} de {} chances".format(vidas-nvidas, vidas) ) # %d feels, format é um metodo de string aparentemente
	#print("tens {0} de {1} chances".format(vidas-nvidas, vidas) ) #alternaticamente da pra escolher a ordem

	chute   = input("manda o numero \n") 	#inputs sao sempre considerados string
	chute   = int(chute)										#essa função converte pra int

	if (chute < 1 or chute > 100):
		print("chute invalido filhx da puta")
		continue 												#pula pra proxima iteracao do loop

	acertou = chute == num_secreto		#atribuicao de bool
	maior   = chute > num_secreto
	menor   = chute < num_secreto


	print("digitaste", chute)

	if (acertou):
		print("acertaste, otario")
		print("fizeste {} pontos".format(pontos))
		break
	else:
		print("erraste, lindo.", end = " ")
		if (maior): 			
			print('alto demais fera')        	#tanto " " quanto ' ' servem pra delimitar uma string
		elif (menor):								#elif é literalmente igual o else if do C
			print("too low mr gamer")
		pontos = abs(pontos - chute) 		#abs() de absoluto, transforma qualquer numero em positico
	
	print()
	print()
	
	#nvidas = nvidas +1
			
print("GAME OVER")
print("resultados")
print("	o numero secreto era", num_secreto)
print("	sua pontuação final foi", pontos)


