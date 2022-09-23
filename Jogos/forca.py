def jogar():
    print("******************************")
    print("**Bem vindo ao jogo da Forca**")
    print("******************************")

    palavra_secreta = "maconha"
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_"]

    acertou = False
    enforcou = False

    print(letras_acertadas)

    while(not acertou and not enforcou):
        chute = input("Escolha uma letra: ").lower().strip()

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

if(__name__ == "__main__"):
    jogar()