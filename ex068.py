# par ou impar
from random import randint
cont = 0

print('=-=-= JOGO DO PAR OU ÍMPAR =-=-=')
print('\n')

while True:
    ejogador = int(input('escolha um número: '))
    parimpar = ' '
    while parimpar not in 'PpIi':
        parimpar = str(input('par ou ímpar? [P/I] ')).strip().upper()[0]
    print('\n')
    ecomputador = randint(0, 11)
    soma = ejogador + ecomputador
    pi = 'PAR'
    if soma % 2 != 0:
        pi = 'ÍMPAR'
    if soma % 2 != 0 and parimpar == 'P':  # se a soma for impar e o jogador escolheu par, terminar
        print(f'o jogador escolheu {ejogador} e o computador escolheu {ecomputador}. total de {soma}, deu {pi}')
        print('-=' * 16)
        print('você perdeu!')
        print('-=' * 16)
        break
    if soma % 2 == 0 and parimpar == 'I':  # se a soma for par e o jogador escolher impar, terminar
        print(f'o jogador escolheu {ejogador} e o computador escolheu {ecomputador}. total de {soma}, deu {pi}')
        print('-=' * 16)
        print('você perdeu!')
        print('-=' * 16)
        break
    if soma % 2 != 0 and parimpar == 'I':  # vitória
        cont += 1
        print(f'o jogador escolheu {ejogador} e o computador escolheu {ecomputador}. total de {soma}, deu {pi}')
        print('-=' * 16)
        print('você ganhou!!!!!')
        print('-=' * 16)
        print('vamos jogar novamente...')
        print('\n')
    if soma % 2 == 0 and parimpar == 'P':  # vitória
        cont += 1
        print(f'o jogador escolheu {ejogador} e o computador escolheu {ecomputador}. total de {soma}, deu {pi}')
        print('-=' * 16)
        print('você ganhou!!!!!')
        print('-=' * 16)
        print('vamos jogar novamente...')
        print('\n')
print('\n\n')
print(f'GAME OVER! você venceu {cont} vezes.')
