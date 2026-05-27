#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste anguloUm professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
from math import cos, tan, sin

x = float(input('Digite o valor do angulo:'))

pi = 3.14

rad = x * (pi / 180.0)

print('cos({}) = {}'.format(x, cos(rad)))
print('sen({}) = {}'.format(x, sin(rad)))
print('tg({}) = {}'.format(x, tan(rad)))