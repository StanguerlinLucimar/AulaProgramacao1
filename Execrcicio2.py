#Crie um programa que recebe dois valores inteiros 
# A e B pelo teclado e imprime o valor de A dividido 
# por B. Entretanto, se o valo de B for 0, imprima 
# uma mensagem de erro e não faça a divisão.
Valor_A = int (input ("Digite Valor A:\n"))
Valor_B= int (input ("Digite Valor B:\n"))


if Valor_B == 0:
    print ("Valor não pode ser Zero")
else: 
    print ("O resultado é", Valor_A + Valor_B )
    input()