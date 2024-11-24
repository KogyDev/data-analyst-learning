# Inventário inicial do jogador
jogador = {"ouro": 100, "inventario": []}

# Itens disponíveis na loja
loja = {
    "Espada Mágica": 50,
    "Poção de Vida": 30,
    "Escudo Encantado": 40,
    "Anel de Invisibilidade": 70
}

print("\n--- Bem-vindo à Loja de Itens Mágicos ---")

# Loop infinito da loja
while True:
    print("\nO que você gostaria de fazer?")
    print("1. Ver itens disponíveis para compra")
    print("2. Ver seu inventário")
    print("3. Vender um item")
    print("4. Sair da loja")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":  # Ver itens disponíveis
        print("\n--- Itens disponíveis na loja ---")
        for item, preco in loja.items():
            print(f"{item}: {preco} ouro")
        
        compra = input("\nQual item você quer comprar? (ou digite 'voltar' para retornar): ").title()
        
        if compra in loja:
            if jogador["ouro"] >= loja[compra]:
                jogador["ouro"] -= loja[compra]
                jogador["inventario"].append(compra)
                print(f"Você comprou {compra}! Seu saldo agora é {jogador['ouro']} ouro.")
            else:
                print("Você não tem ouro suficiente para comprar esse item.")
        elif compra == "Voltar":
            continue
        else:
            print("Esse item não está disponível.")
    
    elif escolha == "2":  # Ver inventário
        print("\n--- Seu inventário ---")
        if jogador["inventario"]:
            for item in jogador["inventario"]:
                print(f"- {item}")
            print(f"Ouro restante: {jogador['ouro']}")
        else:
            print("Seu inventário está vazio.")
    
    elif escolha == "3":  # Vender um item
        print("\n--- Seus itens para venda ---")
        if jogador["inventario"]:
            for i, item in enumerate(jogador["inventario"], 1):
                print(f"{i}. {item}")
            
            venda = input("Digite o nome do item que deseja vender (ou 'voltar' para cancelar): ").title()
            if venda in jogador["inventario"]:
                jogador["inventario"].remove(venda)
                jogador["ouro"] += loja.get(venda, 20)  # Venda vale 20 ouro se o item não estiver listado na loja
                print(f"Você vendeu {venda}! Seu saldo agora é {jogador['ouro']} ouro.")
            elif venda == "Voltar":
                continue
            else:
                print("Você não possui esse item para vender.")
        else:
            print("Seu inventário está vazio, nada para vender.")
    
    elif escolha == "4":  # Sair da loja
        print("\nObrigado por visitar a Loja de Itens Mágicos! Volte sempre!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
