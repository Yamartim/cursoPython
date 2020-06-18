import jogaradivinhation
import jogarforca
#from .. import c2aula1a7 #funcionaria se fosse um "package"

def letsplay():
	print("7#@--------------------------------@#7")
	print("GAMER GANG: here come the gaymes")
	print("7#@--------------------------------@#7")

	print("0: forca")
	print("1: adivinhação")

	select = int(input("pick your poison: "))

	if(select == 0):
		jogarforca.play()
		#c2aula1a7.play()
	elif(select == 1):
		jogaradivinhation.play()
	else:
		print("ah mano sei la entao lmao")
		
	print()

if(__name__ == '__main__'):
	letsplay()