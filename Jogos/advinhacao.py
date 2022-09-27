import random


def jogar():
    print("*******************************")
    print("Bem vindo ao jogo da advinhação")
    print("*******************************")

    numero_secreto: int = random.randrange(1, 101)
    pontos: int = 1000

    print("Selecione o nível de dificuldade:")
    print("[1]Fácil [2]Médio [3]Difícil")
    nivel: int = int(input())

    if nivel == 1:
        total_de_tentativas: int = 10
        print(
            f"Você escolheu a dificuldade Fácil e tem {total_de_tentativas} tentativas"
        )
    elif nivel == 2:
        total_de_tentativas: int = 8
        print(
            f"Você escolheu a dificuldade Médio e tem {total_de_tentativas} tentativas"
        )
    elif nivel == 3:
        total_de_tentativas: int = 6
        print(
            f"Você escolheu a dificuldade Difícil e tem {total_de_tentativas} tentativas"
        )
    else:
        total_de_tentativas: int = 1
        print("Opção inválida :D Então agora você tem apenas 1 tentativa")

    while total_de_tentativas > 0:
        numero_do_usuario: int = int(input("Advinhe o número secreto entre 1 e 100\n"))
        print("Você digitou", numero_do_usuario)

        if numero_do_usuario < 1 or numero_do_usuario > 100:
            print("Você deve digitar um número entre 1 e 100")
            continue

        acerto: int = numero_do_usuario == numero_secreto
        erro_maior: int = numero_do_usuario > numero_secreto

        if acerto:
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if erro_maior:
                print("Você errou! Seu palpite foi maior que o número secreto.")
            else:
                print("Você errou! Seu palpite foi menor que o número secreto.")

        pontos_perdidos: int = abs(numero_secreto - numero_do_usuario)
        pontos = pontos - pontos_perdidos
        total_de_tentativas = total_de_tentativas - 1
        if total_de_tentativas > 1:
            print(f"Você ainda tem {total_de_tentativas} tentativas")
        elif total_de_tentativas == 1:
            print(f"Você ainda tem {total_de_tentativas} tentativa")
        else:
            print(
                f"Você não tem mais tentativas. O número secreto era {numero_secreto}."
            )

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
