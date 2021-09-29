from random import randint
import time
print('''
================ Jogo da adivinhação ==============
Tente adivinhar o número que o computador escolheu!''')
time.sleep(1)
n = int(randint(0,10))
p = 0
t = 0
while p != n:
    p = int(input('Digite um número de 0 a 10: '))
    t += 1
    if p == n:
        print(f'Muito bem, você acertou em {t} tentativa(s)!')
    elif p <= n:
        print('Errou, tente um valor mais ALTO')
    else:
        print('Errou, tente um valor mais BAIXO')
print('Fim do jogo')
            
