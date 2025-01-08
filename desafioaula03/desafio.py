total_gasto = 0
contador_produtos_acima_1000 = 0
produto_mais_barato = ""
preco_mais_barato = float('inf') 

while True:

    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input(f"Digite o preço de {nome_produto}: R$ "))
    
    total_gasto += preco_produto
    
    if preco_produto > 1000:
        contador_produtos_acima_1000 += 1
    
    if preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto
    
    continuar = input("Deseja continuar inserindo produtos? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nResumo da Compra:")
print(f"Total gasto: R$ {total_gasto:.2f}")
print(f"Quantidade de produtos que custam mais de R$1000: {contador_produtos_acima_1000}")
print(f"Produto mais barato: {produto_mais_barato} (R$ {preco_mais_barato:.2f})")