


quant = int(input("Quantos produtos você terá na lista?"))
listaDeCompras = []
for i in range(0,quant):
    listaDeCompras.append(input("Digite o produto:"))
print("Lista de compras:")
for item in listaDeCompras:
     print(item)
input ()   