#Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se
#  será necessário ou não realizar o Grau C (considere o sistema de avaliação da Unisinos, 
# sendo o GA valendo 30% e o GB valendo 70%). Caso algum valor informado seja negativo, informe 
# uma mensagem de erro e não realize o cálculo.

Valor_Grau_A = float (input ("Digite Valor do Grau A (0 a 10):\n"))

if Valor_Grau_A< 0 or  Valor_Grau_A > 10 :
    print ("Valor invalido")
    input()
    exit ()
Valor_Grau_B = float (input ("Digite Valor do Grau B (0 a 10):\n"))

if Valor_Grau_B < 0 or  Valor_Grau_B > 10 :
    print ("Valor invalido")
    input()
    exit ()

Peso_Grau_A = Valor_Grau_A * 0.3
Peso_Grau_B = Valor_Grau_B * 0.7

if Peso_Grau_A + Peso_Grau_B >= 6 :
    print ("Aluno Nao Precisar Realizar Grau C : Nota", Peso_Grau_A + Peso_Grau_B)
else :
    print ("Aluno Precisa Realizar Grau C : Nota", Peso_Grau_A + Peso_Grau_B)
input()   
