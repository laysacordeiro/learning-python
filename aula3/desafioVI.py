#Desafio 6: Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria paa pinta-la. sabendno que cada litro de tinta pinta 2m2.

largura = float(input('Digite a largura da sua parede(em metros): '))
altura = float(input('Digite a altura da sua parede(em metros): '))

area = largura * altura

qtd_tinta = area / 2

print('Sua parede tem {} m². Para pinta-la você precisa de aproximadamente {} L.'.format(area, qtd_tinta))

