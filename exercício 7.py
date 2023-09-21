produto = []
estoque = []
valor = []

concluir = False

while (not concluir):
    print("Digite o nome do produto: ")
    nomeproduto = input()
    print("Digite o Valor do Produto: ")
    ValorProduto = input()
    print("Digite a quantidade que tem no estoque: ")
    EstoqueProduto = input()
    
    produto.append(nomeproduto)
    valor.append(ValorProduto)
    estoque.append(EstoqueProduto)

    print("Deseja inserir outra nota? (s/n)")
    concluir = input() == "n"

print("Segue abaixo todos os respectivos produtos")

for i in range(len(produto)):
    print(f"{produto[i]} : {valor[i]} : {estoque[i]}")


import os 

filename = "arquivo.txt"
file = open(filename, 'w')

for y in range(len(produto)):
    outputline = f"Produto: {produto[y]}\nEstoque do produto: {estoque[y]}\nPreços: {valor[y]}\n\n"
    file.write(outputline) 
file.close()

os.system(f"notepad {filename}")

input("Pressione ENTER para finalizar...")


