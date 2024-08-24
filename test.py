n1 = int(input('Digite um valor: '))       # Adicionamos 'int' para que o valor da variável mude de str para inteiro
n2 = int(input('Digite outro valor: '))
s = n1 + n2
# print (' A soma entre ', n1, 'e', n2, 'vale', s)
print ('A soma entre {} e {} vale'.format(n1, n2, s)) # sintax format oferece controle sobre a formatação de números, strings e outros dados, tornando o código mais legível
 
 
 #Desafio:programa que leia algo e mostre seu tipo primitivo
 
n = input('Digite algo: ')
print('É numerico?', n.isnumeric())
print('Só tem espeços?', n.isspace())
print('É decimal?', n.isdecimal())
print('É alfabetico?', n.isalpha())
