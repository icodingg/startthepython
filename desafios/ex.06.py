# exercicio 1        Adivinhando número
from random import randint
from time import sleep
computador = randint (0, 5)    # Computador "pensa"
print('-=-' * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-' * 20)   
jogador = int(input('Em que número eu pensei?')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
    
    
# exercicio 2     Radar eletronico
velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')