#exercicio 1       Manipulating Text
nome = str(input('Digite seu nome completo: ')).strip()          #Strip remove espaços em branco
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))       #upper deixa caracteres em maiúscula
print('Seu nome em minusculas é {}'.format(nome.lower()))       #lower deixa em minúscula
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))    #len conta o tamanho, enquanto ' - nome.count (' ') ' não deixa selecionar os espaços
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))      # find encontra o primeiro espaço, assim contando as primeiras letras de um nome somente



# exercicio 2         Separando digitos
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))



# exercicio 3        Verificando as primeiras letras de um texto
cid = str(input('Em que cidade você nasceu? ')).strip()     # Removendo espaços para evitar erros
print('Começa com santo?')
print(cid[0:5].upper() == 'SANTO')          # Colocando em letra maiuscula para a comparação ser confiavel


# exercicio 4        Procurando uma string dentro de outra
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Oliveira? {}'.format('oliveira' in nome.lower()))      # in : operador



# exercicio 5    primeira e ultima ocorrência de uma string
frase = str(input('Digite uma frase: ')).upper().strip()
print(' A letra A aparece {} vezes na frase.'.format(frase.count('A')))        # Contando a letra 
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))       # Buscando a primeira referencia
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))       # Começa de traz para frente


# exercicio 6        Primeiro e ultimo nome
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()           #fatiando a string com split
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))              # descobrindo quantos nomes tem com a função len
