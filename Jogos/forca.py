import random


def jogar():
    print("******************************")
    print("**Bem vindo ao jogo da Forca**")
    print("******************************")

    lista_de_palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            lista_de_palavras.append(linha)

    index = random.randrange(0, len(lista_de_palavras))
    palavra_secreta = lista_de_palavras[index]

    letras_acertadas = ["_" for letra in palavra_secreta]

    acertou = False
    enforcou = False
    tentativas = 6

    print(letras_acertadas)

    while not acertou and not enforcou:
        chute = input("Escolha uma letra: ").lower().strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
            print(letras_acertadas)

        else:
            tentativas -= 1
            print(f"Letra {chute.upper()} não encontrada. Ainda faltam {tentativas} tentativas")
            print(letras_acertadas)

        if tentativas <= 0:
            enforcou = True
            print("Você Perdeu ...")

        if "_" not in letras_acertadas:
            acertou = True
            print("Você ganhou !!!")


if __name__ == "__main__":
    jogar()
