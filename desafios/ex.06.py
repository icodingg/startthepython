# exercicio 1        Adivinhando número
from random import randint
from time import sleep
computador = randint (0, 5)    # Computador "pensa"
print('-=-' * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-' * 20)   
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('\033[1;31;43mPROCESSANDO...\033[m')
sleep(3)
if jogador == computador:
    print('PARABÉNS! pensei no número {} e conseguiu me vencer'.format(computador))
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
    
    


# exercicio 2     Radar eletronico
velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:           # condicional para multar caso exceda a velocidade
    print('Multado! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7             #   criando o valor da multa a partir da velocidade excedente
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')




# exercicio 3      Par ou ímpar
numero = int(input('Digite um número: '))
if numero % 2 == 0:           #   O resto da divisão = 0 sempre será PAR
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))



#  exercicio 4      Custo de viagem
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:            # Acrescentando uma diferença de preço a partir de km percorrido
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))



#  exercicio 5     Ano bissexto
ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:        # expressão para resultar anos BISSEXTOS
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))



#   exercicio 6      Maior e Menor valor
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))



#  exercicio 7        Aumento de salário
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:               # salários menores que R$1250,00 ganham 15% de aumento
    novo = salario + (salario * 15 / 100)
else:                             # salários maiores ganham 10
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a receber R${:.2f} agora.'.format(salario, novo))



#   exercicio 8       Analisando triângulo
print('-'*20)
print('Analisador de Triângulos')
print('-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:                       # calculando lados para resultado de triângulo
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
