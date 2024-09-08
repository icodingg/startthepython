# exercicio 1    criar contagem regressiva.
import emoji
from time import sleep
print('{:=^40}'.format('\U00002764, \U0001F680  CONTAGEM REGRESSIVA ANO NOVO 2024 \U0001F680, \U00002764'))
print('-=' * 20)
for c in range(5, 0, -1):      #   ' c ' é a contagem. ' 5 ' o inicio e '0' o fim. '-1' a regressiva
    sleep(0.7)
    print('{}'.format(c), end = '')        # end mantem na mesma linha o print da sequencia
    print('\U000023F3')
sleep(1)
print('\U0001F389 FELIZ ANO NOVOOO! \U0001F389')
sleep(2)
print('\n\n')   # Quebrar linha 



# exercicio 2        Contagem de números pares
print('{:=^40}'.format('APRESSENTANDO OS NÚMEROS PARES'))
print('-=' * 18)
sleep(1)
for c in range(0, 52, 2):
    print('{}'.format(c))
    sleep(0.3)
sleep(1)
print('Te apresentei uma contagem até 50 onde imprimo os números pares. \U0001F60E')
