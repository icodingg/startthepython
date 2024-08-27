from random import choice, shuffle
from math import trunc, hypot, sin, radians, cos, tan    # importando especificamento métodos, podendo também chamar o comando math completo
# exercicio 1         Quebrando um numero real
num = float(input('Digite um valor: '))
print ('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))   #chamando a função trunc para quebrar o número informado



# exercicio 2     Lendo comprimento do cateto oposto e cateto adjacente de um triangulo retangulo. 
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)       #   calculando a hipotenusa
print('A hipotenusa vai medir {:.2f}'.format(hi))



# exercicio 3      Seno, Cosseno e Tangente
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))                                  #   calculando o seno de Radiano
print ('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))                               #    calculando o cosseno de radiano
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))                               #   calculando o tangente de radiano
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))




# exercicio 4         Escolhendo um aluno
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)          # Chamando a função 'randomizador' choice sendo uma escolha dentro da lista
print('O aluno escolhido foi {}'.format(escolhido))



# exercicio 5     Sorteando ordem de lista
n1 = str(input('Primeiro funcionário: '))
n2 = str(input('Segundo funcionário: '))
n3 = str(input('Terceiro funcinário: '))
n4 = str(input('Quarto funcionário: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de funcionários será ')
print(lista)


