import random

# Status inicial do herói
heroi = {"nome": "Aventureiro", "vida": 100, "ataque": 20, "defesa": 10}

# Função para criar um monstro aleatório
def gerar_monstro():
    return {"nome": "Monstro", "vida": random.randint(50, 100), "ataque": random.randint(10, 25)}

# Inicia o loop infinito
while True:
    print("\n--- Uma batalha começou! ---")
    monstro = gerar_monstro()
    print(f"Você encontrou um {monstro['nome']} com {monstro['vida']} de vida.")
    
    while monstro["vida"] > 0:
        print(f"\n{heroi['nome']}: {heroi['vida']} de vida | {monstro['nome']}: {monstro['vida']} de vida")
        print("1. Atacar")
        print("2. Defender")
        print("3. Fugir")
        escolha = input("O que você quer fazer? ")
        
        if escolha == "1":  # Atacar
            dano = heroi["ataque"]
            monstro["vida"] -= dano
            print(f"Você atacou o {monstro['nome']} causando {dano} de dano!")
        
        elif escolha == "2":  # Defender
            reducao = heroi["defesa"]
            print(f"Você se defendeu! O próximo ataque será reduzido em {reducao}.")
        
        elif escolha == "3":  # Fugir
            print("Você fugiu da batalha!")
            break
        
        else:
            print("Escolha inválida, tente novamente.")
            continue
        
        # Monstro contra-ataca
        if monstro["vida"] > 0:
            dano_monstro = max(0, monstro["ataque"] - (heroi["defesa"] if escolha == "2" else 0))
            heroi["vida"] -= dano_monstro
            print(f"O {monstro['nome']} atacou você causando {dano_monstro} de dano!")
        
        # Verifica se o herói morreu
        if heroi["vida"] <= 0:
            print("Você foi derrotado! Fim de jogo.")
            exit()
    
    # Após derrotar o monstro ou fugir, oferece continuar ou sair
    if heroi["vida"] > 0:
        continuar = input("\nDeseja continuar explorando? (s/n): ").lower()
        if continuar != "s":
            print("Você decidiu parar sua aventura. Até a próxima!")
            break
