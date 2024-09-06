# exercicio 1       testando condicionais aninhadas
nome = str(input('Qual é seu nome? '))
#   criando condicionais de diferentes nomes para retornar ao usuario
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Marcos' or nome == 'Paulo':
    print('Seu nome é bem popular.')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é normal.')
print('Tenha um bom dia, {}'.format(nome))



# exercicio 2           Aprovando Empréstimo
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))        
prestacao = casa / (anos * 12)       #    Armazenando valor de prestacao
minimo = salario * 30 / 100        #   Definindo um minimo para ser aprovado
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')



# exercicio  3      Conversor de Bases Numéricas
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases da conversão:
[ 1 ]  converter para BINÁRIO
[ 2 ]  converter para OCTAL
[ 3 ]  converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:               #    Em programação as lingaguens costumam ter operações facilitando o calculo
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
         print ('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Escolha entre as opções acima.')





# exercicio 4     Comparando números
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')




# exercicio 5      Alistamento militar
from datetime import date           #Importando data 
atual = date.today().year           #selecionando ano
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Faltam {} anos para o alistamento'.format(saldo))
elif idade > 18:    
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))

    


# exercicio 6       Calculando média de um aluno
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno está de RECUPERAÇÃO!')
elif media < 5:
    print('O aluno está REPROVADO')

elif media >= 7:
    print('O aluno está APROVADO')



# exercicio 7       Classificando Atletas
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM.')
elif idade <= 14:
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print('Classificação: JUNIOR.')
elif idade <= 25:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER.')



#exercicio 8       Analisando Triângulos 2.0
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:                       # calculando lados para resultado de triângulo
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if r1 == r2 == r3:
        print('EQUILÂTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else: 
        print('ISÓSCELES') 
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
