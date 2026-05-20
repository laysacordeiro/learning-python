#Desafio 1: Faça um programa que leia um numero inteiro e mostre seu sucessor e seu antecessor.
num = int(input('Digite um numero inteiro:'))

ant = num - 1
suc = num + 1

print('O antecessor do numero {} é {} e seu sucessor é {}'.format(num, ant, suc))