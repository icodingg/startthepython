#exercício 1         antecessor e sucessor
n = int(input('Digite um número:')) 
n1 = n + 1
n2 = n - 1
print('O numero digitado é', n, ', seu sucessor é', n1, 'e seu antecessor:', n2)

#exercício 2        operaçoes
n = float(input('Digite um número:'))
n1 = n * 2
n2 = n * 3
n3 = n ** (1/2)
print('o número digitado é {}, o dobro é {}, o triplo {} e a raiz quadrada {}'.format(n,n1,n2,n3))

#exercício 3         mostrar o calculo e média de um aluno
n = float(input('Digite sua nota de exatas:'))
n1 = float(input('Digite sua nota de humanas'))
s = n + n1
m = s / 2
print('Em Exatas nota: {} \n Em Humanas nota: {} \n Calculo das notas: {} \n Assim ficando com a média de {}'.format(n,n1,s,m))

#exercício 4        Ler em metros e transformar para centimetros e milimetros
a = float(input('Digite sua altura:'))
c = a * 100
m = a * 1000
print('Sua alturo é de {} metros \n sendo {} centimetros \n {} milimetros'.format(a, c, m))



