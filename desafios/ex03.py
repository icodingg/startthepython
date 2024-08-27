import math

#exercicio 1       conversor de celsius e fahrenheit
c = float(input('Informe a temperatura em °C: '))
f = 9 * c /5 + 32        #    Calculo para conversão
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))



#exercicio 2       aluguel de carros
dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
pago = (dias * 60) + (km * 0.15)          # Neste caso a diaria do aluguel seria de R$ 60,00 e a cada km percorrido seria R$ 0,15
print ('O total a pagar é de R${:.2f}'.format(pago))



#exercicio 3             utilizando módulos 
num = int(input('Digite um número'))
raiz = math.sqrt(num)                 # importando a biblioteca math (matematica) para operações
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
