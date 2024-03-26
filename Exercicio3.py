#Crie um programa que recebe um valor inteiro referente a um determinado ano.
#  Imprima na tela se o ano informado é bissexto ou não 
# (para simplificar, você pode utilizar apenas a informação de o ano é divisível por 4 ou não).


Ano = int (input ("Digite o Ano:\n"))
if (Ano % 4) ==  0 :
    print ("O Ano", Ano, "é Bissexto")
else :
    print ("O Ano", Ano, "não é Bissexto") 
input()



  
   