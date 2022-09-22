import advinhacao
import forca

print("********************************")
print("********Escolha seu Jogo********")
print("********************************")

print("[1]Advinhação [2]Forca")

jogo = int(input("Qual jogo você quer jogar?\n"))


if(jogo == 1):
    advinhacao.jogar()
elif(jogo == 2):
    forca.jogar()
