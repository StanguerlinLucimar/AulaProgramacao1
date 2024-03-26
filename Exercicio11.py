#Exercício 11. Utilizando while, crie um programa que solicita para o usuário que ele 
# digite 10 valores inteiros. Ao final, imprima a soma de todos os valores digitados. 


Total = 0
NumeroDevalores = 0

while   NumeroDevalores < 10 :
        NumeroDevalores = NumeroDevalores +  1
        ValorDigitado =  int(input("Digite Valor: \n"))
        Total = ValorDigitado + Total

print (Total)
input ()

