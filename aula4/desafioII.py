#Faça um programa que leia o comprimento do cateto adjacente e do cateto oposto de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt

cat_adj = float(input('Digite o valor do cateto adjacente:'))
cat_opt = float(input('Digite o valor do cateto oposto:'))

#ca^2 + co^2 = h^2 => h = raiz quadrada de ca^2 + co^2

hipotenusa = sqrt(cat_adj**2 + cat_opt**2)

print('O valor da hipotenusa é', hipotenusa)