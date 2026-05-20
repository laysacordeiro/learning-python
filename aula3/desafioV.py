#Desafio 5: Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos dolares ela pode comprar

# 1 dolar = 5,02 reais

carteira = float(input('Quanto você tem na carteira?'))
dolar = 0

if carteira < 5.02:
    print('Você não pode comprar nenhum dolar!!')
else:
    while carteira >= 5.02:
        carteira = carteira - 5.02
        dolar+=1

    print('Você pode compra {} dolar(es)'.format(dolar))