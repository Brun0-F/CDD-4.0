from random import randint
itens = ("Pedra","Papel","Tesoura")
computador = randint (0,2)
jogador = int(input("Digite [0] para Pedra , [1] para Papel e [2] para tesoura :"))
if jogador >= 0 and jogador <= 2:
    print (f'O computador escolheu : {itens[computador]}')
    print (f'O jogador escolheu : {itens[jogador]}')
    if computador == 0:
        if jogador == 0:
            print("empate!")
        elif jogador == 1:
            print("Voçe Ganhou!")
        elif jogador == 2:
            print("Computador ganhou!")
    elif computador == 1:
        if jogador == 0:
            print("Computador ganhou!")
        elif jogador == 1:
            print("Empate!")
        elif jogador == 2:
            print("Voçe ganhou!")
    elif computador == 2:
        if jogador == 0:
            print("Voçe ganhou!")
        elif jogador == 1:
            print("computador ganhou!")
        elif jogador == 2:
            print("empate!")
else:
    print("numero invalido!")