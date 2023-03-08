from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
máquina = randint(0, 2)
print('O computador escolheu {}'.format(itens[máquina]))

print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua jogada? '))

print('-=' * 12)
print('A máquina jogou {}'.format(itens[máquina]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 12)

#computador jogou pedra
if máquina == 0: 
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('Jogada inválida!')
#computador jogou papel
elif máquina == 1: 
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('Jogada inválida!')
#computador jogou tesoura
elif máquina == 2: 
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')