from datetime import datetime

class Transaction:
    def __init__(self, valor, categoria, descricao, tipo_transacao, data=None):
        self.valor = valor
        self.categoria = categoria
        self.descricao = descricao
        self.tipo_transacao = tipo_transacao  # "receita" ou "despesa"
        self.data = data if data else datetime.now().strftime("%Y-%m-%d")

class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.categorias_receita = ["Salário", "Freelance", "Outros"]
        self.categorias_despesa = ["Alimentação", "Transporte", "Contas", "Lazer", "Outros"]
    
    def add_transaction(self):
        print("\n=== Adicionar Nova Transação ===")
        
        print("\nSelecione o tipo de transação:")
        print("1. Receita")
        print("2. Despesa")
        
        while True:
            try:
                tipo_escolha = input("Digite a escolha (1-2): ")
                if tipo_escolha == "1":
                    tipo_transacao = "receita"
                    categorias = self.categorias_receita
                    break
                elif tipo_escolha == "2":
                    tipo_transacao = "despesa"
                    categorias = self.categorias_despesa
                    break
                else:
                    print("Escolha inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Tente novamente.")
        
        while True:
            try:
                valor = float(input("\nDigite o valor: R$"))
                if valor <= 0:
                    print("O valor deve ser positivo!")
                    continue
                break
            except ValueError:
                print("Por favor, digite um número válido!")
        
        print("\nCategorias disponíveis:")
        for index, categoria in enumerate(categorias, 1):
            print(f"{index}. {categoria}")
            
        while True:
            try:
                cat_escolha = int(input("Selecione o número da categoria: ")) - 1
                if 0 <= cat_escolha < len(categorias):
                    categoria = categorias[cat_escolha]
                    break
                print("Número de categoria inválido!")
            except ValueError:
                print("Por favor, digite um número válido!")
        
        descricao = input("\nDigite a descrição (opcional): ")
        
        transaction = Transaction(valor, categoria, descricao, tipo_transacao)
        self.transactions.append(transaction)
        print("\nTransação adicionada com sucesso!")
    
    def view_transactions(self):
        if not self.transactions:
            print("\nNenhuma transação encontrada!")
            return
        
        print("\n=== Histórico de Transações ===")
        for index, trans in enumerate(self.transactions, 1):
            print(f"\nTransação {index}:")
            print(f"Tipo: {trans.tipo_transacao.title()}")
            print(f"Valor: R${trans.valor:.2f}")
            print(f"Categoria: {trans.categoria}")
            print(f"Descrição: {trans.descricao or 'Sem descrição'}")
            print(f"Data: {trans.data}")
            print("-" * 30)
    
    def view_summary(self):
        if not self.transactions:
            print("\nNenhuma transação para resumir!")
            return
        
        total_receita = sum(t.valor for t in self.transactions if t.tipo_transacao == "receita")
        total_despesa = sum(t.valor for t in self.transactions if t.tipo_transacao == "despesa")
        saldo = total_receita - total_despesa
        
        print("\n=== Resumo Financeiro ===")
        print(f"Receita Total: R${total_receita:.2f}")
        print(f"Despesa Total: R${total_despesa:.2f}")
        print(f"Saldo Atual: R${saldo:.2f}")
        
        print("\nResumo de Despesas por Categoria:")
        for categoria in self.categorias_despesa:
            total_categoria = sum(t.valor for t in self.transactions 
                               if t.tipo_transacao == "despesa" and t.categoria == categoria)
            if total_categoria > 0:
                print(f"{categoria}: R${total_categoria:.2f}")
    
    def delete_transaction(self):
        self.view_transactions()
        if not self.transactions:
            return
            
        try:
            index = int(input("\nDigite o número da transação para excluir: ")) - 1
            if 0 <= index < len(self.transactions):
                removed = self.transactions.pop(index)
                print(f"\nTransação excluída com sucesso!")
            else:
                print("\nNúmero de transação inválido!")
        except ValueError:
            print("\nPor favor, digite um número válido!")

def main():
    budget = BudgetTracker()
    
    while True:
        print("\n=== Gerenciador Financeiro Pessoal ===")
        print("1. Adicionar Transação")
        print("2. Visualizar Transações")
        print("3. Visualizar Resumo")
        print("4. Excluir Transação")
        print("5. Sair")
        
        choice = input("\nDigite sua escolha (1-5): ")
        
        if choice == "1":
            budget.add_transaction()
        elif choice == "2":
            budget.view_transactions()
        elif choice == "3":
            budget.view_summary()
        elif choice == "4":
            budget.delete_transaction()
        elif choice == "5":
            print("\nObrigado por usar o Gerenciador Financeiro!")
            break
        else:
            print("\nEscolha inválida! Por favor, tente novamente.")

if __name__ == "__main__":
    main()