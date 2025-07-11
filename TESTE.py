import random
#SERVIÇO
def rodadas(jogador1,jogador2):
    if jogador1 == jogador2:
        print('EMPATE')
    elif (jogador1 == 'pedra' and jogador2 == 'tesoura') or (jogador1 == 'papel' and jogador2 == 'pedra') or (jogador1 == 'tesoura' and jogador2 == 'papel'):
        print('Jogador 1 é o vencedor')
    else:
        print('Jogador 2 é o vencedor')


#APRESENTAÇÃO
def pedir_jogo():
    opcoes = ['pedra','papel','tesoura']
    jogada = input("Escolha sua jogada: pedra, papel ou tesoura?").lower()
    while jogada not in opcoes:
        jogada = input("INVÁLIDO.")
    return jogada


#MAIN
def main():
    opcoes = ['pedra','papel','tesoura']
    rodadas = int(input("Escolha quantas rodadas deseja:"))
    vitoria = 0
    vitoria_2 = 0
    empate = 0
    for i in range(1,rodadas + 1):
        print(f"\nRodada {i}:")
        jogador1 = pedir_jogo()
        jogador2 = random.choice(opcoes)
        print(f"Você jogou:{jogador1}")
        print(f"Voce jogou:{jogador2}")
        rodadas = resultado(jogador1,jogador2)

        if resultado == "empate":
            print('EMPATE')
            empate += 1
        elif resultado == "jogador1":
            print("Jogador 1 venceu")
            vitoria += 1
        else:
            print("Jogador 2 venceu")
            vitoria_2 += 1


    print("\nPlacar final:")
    print(f"\nJogador1: {vitoria} vitórias")
    print(f"\nJogador2: {vitoria_2} vitórias")
    print(f"\nempates: {empate}\n")

main()
            
    
    
