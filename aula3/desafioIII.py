#Desafio 3: Escreva um programa que leia um valor em metro e o exiba convertido em centimetros e milimetros.

v = float(input('Digite o valor(em metros) a ser convertido: '))

cm = v * 100
print('{} m = {} cm'.format(v,cm))

mm = v * 1000
print('{} m = {} mm'.format(v,mm))