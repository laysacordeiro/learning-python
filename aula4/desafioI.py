#Crie um programa que leia um numero real e mostre na tela sua porção inteira
from math import trunc

num = float(input('Digite um numero do conjunto real: '))

print('A porção inteira do numero {} é {}'.format(num,trunc(num)))