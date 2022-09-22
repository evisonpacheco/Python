def jogar():
    print("******************************")
    print("**Bem vindo ao jogo da Forca**")
    print("******************************")

    palavra_secreta = "maconha"

    acertou = False
    enforcou = False

    while(not acertou and not enforcou):
        chute = input("Escolha uma letra: ").lower().strip()

        index = 1
        for letra in palavra_secreta:
            if(chute == letra):
                print(f"Encontrei a letra {letra.upper()} na posição {index}")
            index = index + 1


if(__name__ == "__main__"):
    jogar()