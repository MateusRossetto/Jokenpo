from random import randint
from time import sleep
from emoji import emojize

jogadaPC = randint(0,2)
jokenpo = ["papel :hand_with_fingers_splayed:","pedra :raised_fist:","tesoura :victory_hand:"]

while input("Você quer jogar JOKENPO? (s/n) ") == "s":
	posicao = int(input(emojize("Digite 0 para escolsher papel :hand_with_fingers_splayed: \nDigite 1 para escolher pedra :raised_fist: \nDigite 2 para escolher tesoura :victory_hand:\n")))

	print("JO")
	sleep(0.5)
	print("KEN")
	sleep(0.5)
	print("PO")
	sleep(0.5)
	print("Você jogou",(emojize(jokenpo[posicao])), "\nSeu adversário jogou",(emojize(jokenpo[jogadaPC])))

	if jokenpo[posicao] == jokenpo[jogadaPC]:
		print("Vocês empataram!")

	elif jokenpo[posicao] == "papel :hand_with_fingers_splayed:" and jokenpo[jogadaPC] == "tesoura :victory_hand:":
		print("você perdeu!")

	elif jokenpo[posicao] == "papel :hand_with_fingers_splayed:" and jokenpo[jogadaPC] == "pedra :raised_fist:":
		print("Você ganhou!")

	elif jokenpo[posicao] == "pedra :raised_fist:" and jokenpo[jogadaPC] == "papel :hand_with_fingers_splayed:":
		print("Você perdeu!")

	elif jokenpo[posicao] == "pedra :raised_fist:" and jokenpo[jogadaPC] == "tesoura :victory_hand:":
		print("Você ganhou!")

	elif jokenpo[posicao] == "tesoura :victory_hand:" and jokenpo[jogadaPC] == "papel :hand_with_fingers_splayed:":
		print("Você ganhou!")

	elif jokenpo[posicao] == "tesoura :victory_hand:" and jokenpo[jogadaPC] == "pedra :raised_fist:":
		print("Você perdeu!")
	print("---------------------------------")