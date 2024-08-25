import math

#exercicio 1       Solicitar ao usuário o número para a tabuada
n = int(input('Digite um número: '))

# Exibir a introdução da tabuada
print('Tabuada de {}:'.format(n))

# Gerar e exibir a tabuada
for i in range(1, 11):  # Vai de 1 até 10
    resultado = n * i
    print('{} x {} = {}'.format(n, i, resultado))
    



#exercício 2    Saber valor da carteira e quanto poderia comprar em dolar
real = float(input('Quanto tem em carteira?'))
dolar = real / 5.20       #Buscando cotação aproximada da época, divisão de moeda para chegar ao resultado

print('Em conta tenho R$', real)
print('Com R${} o senhor consegue comprar {:.2f} doláres'.format(real,dolar))        #dentro de {dólar}  se coloca :.2f para cortar os numeros pós virgula




#exercício 3       Calcular gasto de tinta para pintar uma parede
altura = float(input('Digite a altura da parede:'))
largura = float(input('Digite a largura da parede:'))

area = altura * largura
tinta = 2
litros = area / tinta

# Arredondar para cima para garantir que há tinta suficiente
litros = math.ceil(litros) #fazendo o import da função math

print('Sua parede tem {:.2f}m², então será necessario {} litros para pintar '.format(area,litros))




#exercicio 4     fazer um algoritmo de desconto
valor = float(input('Qual o valor do produto?'))

desconto = 5 # 5%
valor_desconto = valor * (desconto / 100)    #calcula o valor do desconto
valor_atual = valor - valor_desconto     # calcular o valor com desconto

print ('Valor do produto:{} \n Desconto aplicado:{} \n Valor com desconto:{}'.format(valor,valor_desconto,valor_atual))



#exercicio 5     algoritmo de aumento de salario
salario = float(input('Qual o seu salario?'))

aumento = 15
valor_aumento = salario * (aumento / 100)
salario_atual = salario + valor_aumento

print('Seu salario de R${} tera um aumento de {} e ficará {}'.format(salario,valor_aumento,salario_atual))

