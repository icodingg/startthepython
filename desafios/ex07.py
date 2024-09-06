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
