# + adição
# - subtração
# * multiplicação
# / divisão
# ** potenciação
# // divisão inteira
# % resto da divisão

#para testar se uma coisa é igual a outra usamos ==. ja para atribuição de valor é =

#ordem de precedencia: 1: (); 2: **; 3: *, /, //, %; 4: +,-.

#ax + b = c

print('ax + b = c')

a = int(input("Digite o valor de A na sua equação:"))
b = int(input("Digite o valor de B na sua equação:"))
c = int(input("Digite o valor de C na sua equação:"))

if(a == 0):
    print("A equação não é do primeiro grau.")
elif(b > 0):
    b = b * (-1)
    x = (c + b) / a
    print("O valor de x é: {}".format(x))
else:
    b = b * (-1)
    x = (c + b) / a
    print("O valor de x é: {}".format(x))
