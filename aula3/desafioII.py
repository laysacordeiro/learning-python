#Desafio 2: Crie um algoritmo que leia um numero e mostre seu dobro, tripo e raiz quadrada.

num = int(input('Digite um numero:'))

dobro = num * 2
print('Dobro: ', dobro)

triplo = num * 3
print('Triplo: ', triplo)

i = 1

while i * i <= num:
    if i * i == num:
        print("Raiz:", i)
    i += 1