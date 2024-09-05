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



# exercicio 2   
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')
