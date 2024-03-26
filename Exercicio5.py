# Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a 
# letra é uma vogal ou uma consoante.

LetraDigitada =  (input ("Digite uma letra:\n"))

Vogal = ["A","E","I","O","U"]
for Letra in Vogal:
    if LetraDigitada == Letra :
        print ("Letra é uma Vogal")
        input ()
        exit ()
print ("é uma consoante")
input ()