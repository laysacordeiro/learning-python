#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.

var = input('Escreva algo na tela:')

print('O tipo da variável é ', type(var))
print('A variavel é numerica? ', var.isnumeric())
print('A variavel é alfabetica? ', var.isalpha())
print('A variavel é alfanumerica? ', var.isalnum())
print('A variavel tem todas as letras maiusculas? ', var.isupper())
print('A variavel tem todas as letras minusculas? ', var.islower())
