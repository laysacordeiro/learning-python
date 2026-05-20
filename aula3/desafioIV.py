#Desafio 4: Faça um programa que leia um numero inteiro qualquer e mostre a sua tabuada

n = int(input('Digite um numero inteiro:'))

i = 1

print('Tabuada do ',n)
print('----Adição----')
while i <= 10:
     add = n + i
     print('{} + {} = {}'.format(n, i, add))

     i+=1

print('----Subtração----')
i = 1
while i <= 10:
     sub = n - i
     print('{} - {} = {}'.format(n, i, sub))

     i+=1

print('----Multiplicação----')
i = 1
while i <= 10:
     mult = n * i
     print('{} * {} = {}'.format(n, i, mult))

     i+=1

print('----Divisão----')
i = 1
while n / i >= 1:
     if n % i == 0:
        div = n / i
        print('{} / {} = {}'.format(n, i, div))

     i+=1

print('----Potenciação----')
i = 1
while i <= 10:
     pot = n ** i
     print('{} ** {} = {}'.format(n, i, pot))

     i+=1
